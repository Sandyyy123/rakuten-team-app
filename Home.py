"""Home — project landing. Data & EDA is fully built (Sandeep Grover); other sections are placeholders."""
import os, base64
import streamlit as st
from _shared import page, footer, tiles, raku, CORAL

page("Home", "🛒")
R = raku(); s = R["stats"]

# ---- gradient hero (logo + badge + title in one band) --------------------------
_logo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report_figs", "liora_logo.png")
_img = ""
if os.path.exists(_logo):
    _b = base64.b64encode(open(_logo, "rb").read()).decode()
    _img = f'<img src="data:image/png;base64,{_b}" alt="Liora" style="width:210px;height:auto;display:block;margin:0 0 12px">'

st.markdown(f"""
<div class="rk-hero">
  {_img}
  <span class="rk-badge">Liora MLE · Project 06 · Team project</span>
  <h1 style="margin:14px 0 4px;font-size:2.25rem">Rakuten France — Multimodal Product Classification</h1>
  <p style="font-size:1.1rem;color:#475569;font-weight:600;margin:0 0 6px">
     Sorting 84,916 products into 27 categories from their French titles and photos</p>
  <p style="color:#64748b;margin:0;max-width:760px">
     A team project on the public <b>Rakuten France</b> multimodal classification challenge — predict each
     product's category (<span class="mono">prdtypecode</span>) from its <b>text</b> and its <b>image</b>.
     This app is the interactive restitution, one page per project stage.</p>
</div>
""", unsafe_allow_html=True)

tiles([
    (f"{s['n_products']:,}",             "Products"),
    (str(s["n_classes"]),                "Categories"),
    (f"{s['imbalance_ratio']}×",         "Class imbalance"),
    (f"{s['pct_missing_description']}%", "Missing description"),
    ("~81%",                             "French text"),
])
st.divider()

st.subheader("Project sections")
st.markdown(
    "- ✅ **Data & EDA** — business case, data exploration and text pre-processing *(Sandeep Grover — complete)*\n"
    "- 🚧 **Modelling & Fusion** — classical & deep-learning models + multimodal fusion *(Jonathan Vints — placeholder)*\n"
    "- 🚧 **Image** — image branch / CNN *(Thomas Maisch — placeholder)*\n"
    "- 🚧 **Demo** — live prediction on new input *(team — once models are trained)*\n"
    "- 📄 **Report** — the written project report (PDF / Word)\n"
    "- ❓ **Q&A** — anticipated examiner questions with in-depth answers")

st.markdown('<div class="rk-note"><b>Start here:</b> open <b>Data & EDA</b> in the sidebar — the fully built '
            'section (business case, five statistical findings with figures, and the TF-IDF pre-processing '
            'pipeline). The other stages are placeholders for the teammates to complete.</div>',
            unsafe_allow_html=True)
footer()
