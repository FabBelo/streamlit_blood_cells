from _utils import render_md
import streamlit as st

st.set_page_config(page_title="À propos",
                   page_icon="👥", layout="wide")
st.title("👥 À propos")

render_md("07_A_propos.md", unsafe=False)
