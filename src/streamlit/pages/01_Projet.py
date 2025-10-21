from _utils import render_md
import streamlit as st

st.set_page_config(page_title="Projet",
                   page_icon="🧬", layout="wide")
st.title("🧬 Projet")
st.caption(
    "Classification de cellules sanguines par Computer Vision et Deep Learning")

render_md("01_Projet.md", unsafe=False)
