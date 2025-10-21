from _utils import render_md
import streamlit as st

st.set_page_config(page_title="Modélisation DL",
                   page_icon="🧠", layout="wide")
st.title("🧠 Modélisation DL")
st.caption(
    "Techniques de Deep Learning pour la classification des cellules sanguines")

render_md("04_Modelisation_DL.md", unsafe=False)
