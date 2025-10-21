from _utils import render_md
import streamlit as st

st.set_page_config(page_title="EDA", page_icon="📊", layout="wide")
st.title("📊 EDA – Exploration des données")

render_md("02_EDA.md", unsafe=False)
