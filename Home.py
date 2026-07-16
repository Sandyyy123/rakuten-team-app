"""Home - project landing. Full multi-page walkthrough of the Rakuten multimodal classification project."""
import os, base64
import streamlit as st
from _shared import page, footer, tiles, raku, CORAL, fig

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
  <h1 style="margin:14px 0 4px;font-size:2.25rem">Rakuten France - Multimodal Product Classification</h1>
  <p style="font-size:1.1rem;color:#475569;font-weight:600;margin:0 0 6px">
     Sorting 84,916 products into 27 categories from their French titles and photos</p>
  <p style="color:#64748b;margin:0;max-width:760px">
     A team project on the public <b>Rakuten France</b> multimodal classification challenge - predict each
     product's category (<span class="mono">prdtypecode</span>) from its <b>text</b> and its <b>image</b>.
     This app is an interactive walkthrough of the project, one page per stage.</p>
</div>
""", unsafe_allow_html=True)

tiles([
    (f"{s['n_products']:,}",             "Products"),
    (str(s["n_classes"]),                "Categories"),
    (f"{s['imbalance_ratio']}×",         "Class imbalance"),
    (f"{s['pct_missing_description']}%", "Missing description"),
    ("~81%",                             "French text"),
])

st.subheader("How it works - and who did what")
st.image(fig("pipeline_attrib.png"), use_container_width=True)
st.caption("The full project pipeline, colour-coded by contributor: **Sandeep Grover** (data, EDA, text "
           "preprocessing, website, presentation, report, independent replication), **Jonathan Vints** (classical and transformer "
           "text models), **Thomas Maisch** (image model, multimodal fusion, validation and the challenge "
           "submission → public leaderboard #15, 0.8902).")
st.divider()

st.subheader("Final result")
tiles([
    ("0.8984", "Multimodal weighted-F1"),
    ("#15",    "Public leaderboard (0.8902)"),
    ("0.87",   "Text (XLM-RoBERTa)"),
    ("0.6515", "Image (EfficientNet-B0)"),
    ("0.8144", "Benchmark to beat"),
])
st.caption("Late fusion of the text and image branches is the team's strongest model - see Merge & comparison.")
st.divider()

st.subheader("Project sections")
st.markdown(
    "- ✅ **Data & EDA** - business case, exploration & text pre-processing → TF-IDF *(Sandeep Grover)*\n"
    "- ✅ **Text modelling** - TF-IDF baselines (KNN / XGBoost, BayesSearch) → XLM-RoBERTa · weighted-F1 0.87 *(Jonathan Vints)*\n"
    "- ✅ **Image processing & modelling** - crop → EfficientNet-B0 · weighted-F1 0.6515 *(Thomas Maisch)*\n"
    "- ✅ **Merge & model comparison** - fuse **Text + Image** → weighted-F1 0.8984 *(Thomas Maisch)*\n"
    "- 🔮 **Run the model** - live demo (local or hosted)\n"
    "- 📄 **Report** - the written project report (PDF / Word)\n"
    "- ❓ **Q&A** - anticipated examiner questions with in-depth answers")

st.markdown('<div class="rk-note"><b>Walkthrough:</b> open <b>Data &amp; EDA</b> for the full EDA + TF-IDF '
            'pipeline, then follow <b>Text → Image → Merge</b> to see how the two branches fuse into the '
            '0.8984 multimodal model.</div>', unsafe_allow_html=True)
footer()
