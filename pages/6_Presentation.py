"""Presentation — Sandeep Grover's slide deck for the Data & EDA / pre-processing section."""
import os
import streamlit as st
import streamlit.components.v1 as components
from _shared import page, footer

page("Presentation", "🖥️")
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(BASE, "slides", "presentation.html")

st.title("Presentation")
st.caption("Sandeep Grover · 7-minute slide deck for the business case, data exploration and text "
           "pre-processing section.")

c1, c2 = st.columns([1, 1])
with c1:
    st.link_button("🔳 Open fullscreen (new tab)",
                   "http://82.29.180.70:8090/rakuten-deliverables/Preprocessing_Sandeep_Grover.html",
                   use_container_width=True)
with c2:
    with open(HTML, "rb") as f:
        st.download_button("⬇ Download slides (HTML)", f.read(),
                           file_name="Preprocessing_Sandeep_Grover.html", mime="text/html",
                           use_container_width=True)

st.markdown('<div class="rk-note">Click inside the deck below, then use the <b>← / →</b> arrow keys to move '
            'between slides. For the best view, use <b>Open fullscreen</b> above.</div>',
            unsafe_allow_html=True)

with open(HTML, encoding="utf-8") as f:
    deck = f.read()
components.html(deck, height=760, scrolling=True)
footer()
