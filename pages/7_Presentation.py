"""Presentation - the full team slide deck (business case, data, text, image, multimodal fusion)."""
import os
import streamlit as st
import streamlit.components.v1 as components
from _shared import page, footer

page("Presentation", "🖥️")
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(BASE, "slides", "presentation.html")
PDF = os.path.join(BASE, "downloads", "Rakuten_Presentation.pdf")

st.title("Presentation")
st.caption("The full team slide deck: business case, data exploration, text and image modelling, and "
           "multimodal fusion.")

c1, c2 = st.columns([1, 1])
with c1:
    if os.path.exists(PDF):
        with open(PDF, "rb") as f:
            st.download_button("⬇ Download slides (PDF)", f.read(),
                               file_name="Rakuten_Presentation.pdf", mime="application/pdf",
                               use_container_width=True)
with c2:
    with open(HTML, "rb") as f:
        st.download_button("⬇ Download slides (HTML)", f.read(),
                           file_name="Rakuten_Presentation.html", mime="text/html",
                           use_container_width=True)

st.markdown('<div class="rk-note">Click inside the deck below, then use the <b>← / →</b> arrow keys to move '
            'between slides, or press <b>F</b> for fullscreen. The PDF above is a static copy of all slides.</div>',
            unsafe_allow_html=True)

with open(HTML, encoding="utf-8") as f:
    deck = f.read()
components.html(deck, height=760, scrolling=True)
footer()
