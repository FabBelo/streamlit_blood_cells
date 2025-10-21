from _utils import render_md
import streamlit as st

st.set_page_config(page_title="Conclusions",
                   page_icon="🎓", layout="wide")
st.title("🎓 Conclusions du projet Bloodifier")

render_md("06_Conclusions.md", unsafe=False)
