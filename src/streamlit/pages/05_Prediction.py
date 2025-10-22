# -*- coding: utf-8 -*-
# Fichier suggéré : src/streamlit/pages/05_Prediction.py

from pathlib import Path
import io
import numpy as np
import streamlit as st
from PIL import Image, ImageOps
import tensorflow as tf

# -----------------------------
# Constantes / chemins projet
# -----------------------------
CLASS_NAMES = [
    "Basophile",
    "Éosinophile",
    "Érythroblaste",
    "Granulocyte immature",
    "Lymphocyte",
    "Monocyte",
    "Neutrophile",
    "Plaquette",
]

PAGE_DIR = Path(__file__).resolve().parent
STREAMLIT_DIR = PAGE_DIR.parent
SRC_DIR = STREAMLIT_DIR.parent
REPO_ROOT = SRC_DIR.parent
MODELS_DIR = REPO_ROOT / "models"
MODEL_PATH = SRC_DIR / "densenet201_blood_cells.keras"

INPUT_SIZE = (224, 224)  # redimensionnement unique

# Lien Google Drive fourni
MODEL_GDRIVE_URL = "https://drive.usercontent.google.com/download?id=1anA_pok_6_iR7yuEFHEfzLgkJYU4aF-f"

# -----------------------------
# Mise en page
# -----------------------------
st.set_page_config(page_title="Prédiction",
                   page_icon="🎯", layout="wide")
st.title("🎯 Prédiction sur une image")
st.caption("Flux : upload → aperçu & caractéristiques → inférence → résultat.")

# ------------------------------------------------------------
# Utilitaires téléchargement
# ------------------------------------------------------------


@st.cache_data(show_spinner=False)
def _download_with_gdown(file_id: str, dst_path: str) -> bool:
    """Essaye gdown si dispo. Retourne True si succès."""
    try:
        import gdown  # type: ignore
    except Exception:
        return False
    try:
        url = MODEL_GDRIVE_URL
        gdown.download(url, dst_path, quiet=True)
        return os.path.exists(dst_path) and os.path.getsize(dst_path) > 0
    except Exception:
        return False


def _download_with_requests(file_id: str, dst_path: str) -> None:
    """Téléchargement Google Drive (fallback) avec barre de progression."""
    session = requests.Session()
    url = "https://drive.google.com/uc?export=download"
    params = {"id": file_id}

    # 1er hit : peut nécessiter un token de confirmation (fichiers volumineux)
    response = session.get(url, params=params, stream=True)
    token = None
    for k, v in response.cookies.items():
        if k.startswith("download_warning"):
            token = v
            break
    if token:
        params["confirm"] = token
        response = session.get(url, params=params, stream=True)

    total = int(response.headers.get("Content-Length", 0)) or None
    chunk = 32768

    progress = st.progress(0)
    downloaded = 0
    with open(dst_path, "wb") as f:
        for data in response.iter_content(chunk_size=chunk):
            if not data:
                continue
            f.write(data)
            downloaded += len(data)
            if total:
                progress.progress(min(int(downloaded / total * 100), 100))
    progress.empty()


def ensure_model_downloaded(local_path: Path, gdrive_url: str) -> Path:
    """Télécharge le modèle si absent ou vide. Retourne le chemin local final."""
    if local_path.exists() and local_path.stat().st_size > 0:
        return local_path

    file_id = _extract_gdrive_file_id(gdrive_url)
    if not file_id:
        st.error(
            "Impossible d'extraire l'ID du fichier Google Drive depuis l'URL fournie.")
        st.stop()

    st.info("Téléchargement du modèle depuis Google Drive…")
    with st.spinner("Téléchargement en cours…"):
        ok = _download_with_gdown(file_id, str(local_path))
        if not ok:
            _download_with_requests(file_id, str(local_path))

    if not local_path.exists() or local_path.stat().st_size == 0:
        st.error("Échec du téléchargement du modèle.")
        st.stop()

    st.success("Modèle téléchargé avec succès. ✅")
    return local_path

# ------------------------------------------------------------
# Cache du modèle (chargement unique)
# ------------------------------------------------------------


@st.cache_resource(show_spinner=False)
def load_model_cached(model_path: str):
    return tf.keras.models.load_model(model_path, compile=False)


def labels_from_model(model, fallback):
    labels_path = MODELS_DIR / "class_labels.txt"
    if labels_path.exists():
        return [l.strip() for l in labels_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    n = int(getattr(model, "output_shape", [None, None])[-1] or len(fallback))
    lab = getattr(model, "classes_", None)
    if isinstance(lab, (list, tuple)) and len(lab) == n:
        return list(lab)
    return fallback[:n] if len(fallback) >= n else [f"class_{i}" for i in range(n)]


def run_inference(model, x):
    preds = model.predict(x, verbose=0)
    preds = np.squeeze(np.array(preds, dtype=np.float32))
    if preds.ndim == 1:
        s = float(preds.sum())
        if s <= 0.0 or s > 1.0001:
            e = np.exp(preds - np.max(preds))
            preds = e / e.sum()
    return preds


def basic_image_stats(img, raw_bytes):
    """Affiche quelques infos simples sur l'image."""
    arr = np.array(img.convert("L"), dtype=np.uint8)
    h, w = arr.shape
    size_kb = len(raw_bytes) / 1024.0
    mean = float(arr.mean())
    std = float(arr.std())
    return [
        f"• Dimensions : **{w}×{h}** px",
        f"• Taille fichier : **{size_kb:.1f} kB**",
        f"• Mode/Format : **{img.mode}**",
    ]


# -----------------------------
# 1) Upload
# -----------------------------
uploaded = st.file_uploader(
    "Choisissez une image de cellule (JPG/PNG/TIFF)",
    type=["jpg", "jpeg", "png", "tif", "tiff"],
    accept_multiple_files=False,
)

# Réinitialiser le résultat si nouvelle image
if uploaded is not None:
    st.session_state.pop("pred_probs", None)
    st.session_state.pop("pred_label", None)
    st.session_state.pop("pred_score", None)

# -----------------------------
# 2) Aperçu & caractéristiques
# -----------------------------
col_left, col_right = st.columns([1.2, 1])
pil_img = None
raw_bytes = None

with col_left:
    if uploaded is None:
        st.info("Téléversez une image pour afficher l’aperçu et lancer l’inférence.")
    else:
        raw_bytes = uploaded.read()
        try:
            pil_img = Image.open(io.BytesIO(raw_bytes))
            pil_img = ImageOps.exif_transpose(pil_img).convert("RGB")
            st.image(pil_img, caption="Image originale",
                     width='stretch')
        except Exception as e:
            st.error(f"Impossible de lire l’image : {e}")
            pil_img = None

with col_right:
    if pil_img is not None and raw_bytes is not None:
        st.markdown("**Caractéristiques**")
        for line in basic_image_stats(pil_img, raw_bytes):
            st.write(line)

# -----------------------------
# 3) Bouton Inférence
# -----------------------------
can_infer = pil_img is not None
infer_btn = st.button("🔮 Inférence", type="primary", disabled=not can_infer)

# -----------------------------
# 4) Exécution : resize → preprocess_input → prédiction
# -----------------------------
if infer_btn and pil_img is not None:
    resized = pil_img.resize(INPUT_SIZE, Image.Resampling.BILINEAR)
    x = np.array(resized, dtype=np.float32)
    x = np.expand_dims(x, axis=0)

    # 🔧 Prétraitement officiel DenseNet201
    x = tf.keras.applications.densenet.preprocess_input(x)

    if not MODEL_PATH.exists():
        st.error(f"Modèle introuvable : `{MODEL_PATH}`")
        st.stop()

    if "keras_model" not in st.session_state:
        with st.spinner("Chargement du modèle Keras…"):
            try:
                model = load_model_cached(str(MODEL_PATH))
                st.session_state["keras_model"] = model
                st.success("Modèle chargé en mémoire. ✅")
            except Exception as e:
                st.error(f"Échec de chargement du modèle : {e}")
                st.stop()
    else:
        model = st.session_state["keras_model"]

    with st.spinner("Inférence en cours…"):
        try:
            probs = run_inference(model, x)
            labels = labels_from_model(model, CLASS_NAMES)
            order = np.argsort(probs)[::-1]
            top_idx = int(order[0])
            top_label = labels[top_idx] if top_idx < len(
                labels) else f"class_{top_idx}"
            top_score = float(probs[top_idx])

            st.session_state["pred_probs"] = probs
            st.session_state["pred_label"] = top_label
            st.session_state["pred_score"] = top_score
        except Exception as e:
            st.error(f"Erreur pendant l’inférence : {e}")
            st.stop()

# -----------------------------
# 5) Résultats
# -----------------------------
if "pred_label" in st.session_state and "pred_score" in st.session_state:
    c1, c2 = st.columns([1, 1])
    with c1:
        st.metric("Classe prédite",
                  st.session_state["pred_label"],
                  delta=f"{st.session_state['pred_score']:.3f}")
    with c2:
        probs = st.session_state["pred_probs"]
        labels = labels_from_model(
            st.session_state["keras_model"], CLASS_NAMES)
        order = np.argsort(probs)[::-1]
        rows = [{"classe": labels[i] if i < len(labels) else f"class_{i}",
                 "proba": float(probs[i])} for i in order]
        st.markdown("**Scores par classe (triés)**")
        st.dataframe(rows, width='stretch', hide_index=True)
