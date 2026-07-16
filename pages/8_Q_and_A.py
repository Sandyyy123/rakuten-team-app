"""Q&A - questions and answers across the whole project (all three members)."""
import os
import streamlit as st
import streamlit.components.v1 as components
from _shared import page, footer

page("Q&A", "❓")
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(BASE, "slides", "qa.html")

st.title("Questions and answers")
st.caption("In-depth questions and answers across the whole project: data and EDA, text pre-processing, "
           "text modelling, and image and multimodal fusion.")

with open(HTML, "rb") as f:
    st.download_button("⬇ Download Q&A (HTML)", f.read(),
                       file_name="Rakuten_Preprocessing_QA.html", mime="text/html",
                       use_container_width=True)

with open(HTML, encoding="utf-8") as f:
    qa = f.read()
components.html(qa, height=1000, scrolling=True)
footer()
