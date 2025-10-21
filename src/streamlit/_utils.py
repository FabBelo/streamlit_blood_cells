# --- dans src/streamlit/_utils.py ---
from pathlib import Path
import re
import streamlit as st

APP_DIR = Path(__file__).parent
CONTENT_DIR = APP_DIR / "content"
ASSETS_DIR = APP_DIR / "assets"


@st.cache_data
def load_md(name: str) -> str:
    return (CONTENT_DIR / name).read_text(encoding="utf-8")


_IMG_MD = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')


def render_md(name: str, unsafe: bool = False):
    """
    Affiche le Markdown en remplaçant les images MD par st.image(assets/...).
    Pas de double rendu, et largeur responsive via width='content'.
    """
    raw = load_md(name)

    i = 0
    for m in _IMG_MD.finditer(raw):
        # 1) texte avant l'image
        before = raw[i:m.start()]
        if before.strip():
            st.markdown(before, unsafe_allow_html=unsafe)

        # 2) image
        alt, path = m.group(1), m.group(2)
        # accepte 'assets/...' ou 'src/streamlit/assets/...'
        fname = Path(path).name
        fpath = ASSETS_DIR / fname
        if fpath.exists():
            st.image(fpath, caption=(alt or None), width="content")
        else:
            st.warning(f"Image introuvable: {path}")

        # 3) caption en italique juste après l'image (optionnelle)
        rest = raw[m.end():]
        cap = re.match(r'^\s*\*([^*]+)\*\s*', rest)
        if cap:
            st.caption(cap.group(1).strip())
            i = m.end() + cap.end()
        else:
            i = m.end()

    # 4) texte après la dernière image
    tail = raw[i:]
    if tail.strip():
        st.markdown(tail, unsafe_allow_html=unsafe)
