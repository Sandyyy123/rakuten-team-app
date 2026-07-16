"""Presentation Minutes (tentative) - speaker minutes + per-slide timing for the 35-slide defence deck."""
import os
import streamlit as st
import streamlit.components.v1 as components
from _shared import page, footer

page("Presentation Minutes", "🗒️")
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(BASE, "slides", "presentation_minutes.html")

st.title("Presentation Minutes (tentative)")
st.caption("Speaker minutes, per-slide timing and handover script for the 35-slide project defence. "
           "Slide ownership and timing are fixed for the team sync; the exact wording on each slide is "
           "each speaker's own.")

with open(HTML, "rb") as f:
    st.download_button("⬇ Download minutes (HTML)", f.read(),
                       file_name="Rakuten_Presentation_Minutes.html", mime="text/html",
                       use_container_width=True)

st.markdown('<div class="rk-note"><b>Tentative</b> - slide ownership and per-slide timing are fixed for '
            'the team sync; the words on each slide are each speaker\'s own. Total scripted time is about '
            '20 minutes (Sandeep 6:40 · Jonathan 5:00 · Thomas 8:20).</div>', unsafe_allow_html=True)

with open(HTML, encoding="utf-8") as f:
    minutes = f.read()
components.html(minutes, height=1000, scrolling=True)
footer()
