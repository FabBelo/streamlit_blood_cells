from _utils import render_md
import streamlit as st

st.set_page_config(page_title="Modélisation ML",
                   page_icon="🤖", layout="wide")
st.title("🤖 Modélisation ML")
st.caption("Une approche simple mais potentiellement efficace")

render_md("03_Modélisation_ML.md", unsafe=False)
