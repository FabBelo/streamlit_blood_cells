# src/streamlit/app.py
from pathlib import Path
from PIL import Image
import streamlit as st

# ------------------------------
# Configuration de la page
# ------------------------------
st.set_page_config(
    page_title="Bloodifier",
    page_icon="🩸",
    layout="wide",
)

# ------------------------------
# Image d'illustration (facultative)
# ------------------------------
APP_DIR = Path(__file__).resolve().parent
ASSETS_DIR = APP_DIR / "assets"
COVER_PATH = ASSETS_DIR / "cover_blood_cells.png"

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    if COVER_PATH.exists():
        st.image(
            str(COVER_PATH),
            caption="Image d’illustration de cellules sanguines (IA générative)",
            use_container_width=True,
        )
    else:
        st.info("Ajoutez une image dans `src/streamlit/assets/cover_blood_cells.png`.")

with col2:
    st.title("🩸 Bloodifier")
    st.markdown(
        """
        ### Plateforme de classification de cellules sanguines
        **Bloodifier** est une application interactive de démonstration, issue du projet de fin de formation *Data Scientist*.
        Elle illustre un pipeline complet de **vision par ordinateur** appliqué à la cytologie sanguine :
        - Prétraitement et **Exploration (EDA)**
        - **Modélisation Machine Learning**
        - **Modélisation Deep Learning**
        - **Prédiction interactive** sur nouvelles images
        - **Conclusions & Bibliographie**
        """
    )

st.markdown("---")

# ------------------------------
# Section navigation
# ------------------------------
st.subheader("Navigation")
st.markdown(
    """
    Vous pouvez naviguer entre les sections grâce au **menu latéral gauche** :
    - 🧬 Projet Bloodifier  
    - 📊 Exploration des données (EDA)  
    - 🤖 Modélisation par ML  
    - 🧠 Modélisation par DL  
    - 🎯 Prédiction  
    - 🎓 Conclusions  
    - 👥 À propos
    """
)

st.markdown("---")

st.caption(
    "© 2025 – Projet Bloodifier, Parcours Data Scientist – Fabien BELLOC & Julien THERIER")
