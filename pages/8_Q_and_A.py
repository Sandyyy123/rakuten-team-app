"""Q&A — anticipated examiner questions for the Data & EDA / pre-processing section."""
import os
import streamlit as st
import streamlit.components.v1 as components
from _shared import page, footer

page("Q&A", "❓")
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(BASE, "slides", "qa.html")

st.title("Q&A — anticipated questions")
st.caption("Sandeep Grover · in-depth answers to likely examiner questions on the business case, data "
           "exploration and text pre-processing (metrics, statistics, TF-IDF, and concepts).")

with open(HTML, "rb") as f:
    st.download_button("⬇ Download Q&A (HTML)", f.read(),
                       file_name="Rakuten_Preprocessing_QA.html", mime="text/html",
                       use_container_width=True)

with open(HTML, encoding="utf-8") as f:
    qa = f.read()
components.html(qa, height=1000, scrolling=True)
footer()
