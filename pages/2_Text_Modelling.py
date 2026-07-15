"""Text modelling - Jonathan Vints (classical ML on TF-IDF -> XLM-RoBERTa)."""
import streamlit as st
from _shared import page, footer, tiles

page("Text Modelling", "🤖")
GH = "https://github.com/DataScientest-Studio/apr26_bds_int_rakuten/tree/Jonathan"

st.title("🤖 Text modelling")
st.caption("Owner: **Jonathan Vints** · from TF-IDF baselines to a fine-tuned multilingual transformer.")

st.markdown(
    '<div class="rk-note"><b>Input:</b> the cleaned text (title + description) and the TF-IDF features '
    'from the <b>Data &amp; EDA</b> stage. <b>Output:</b> the strong text model whose representation is '
    'later fused with the image branch on the <b>Merge &amp; comparison</b> page.</div>',
    unsafe_allow_html=True)

tiles([
    ("0.87",   "Our text model (weighted-F1)"),
    ("0.8113", "Text benchmark"),
    ("XLM-RoBERTa", "Best text model"),
    ("KNN + XGBoost", "Classical baselines"),
])

st.subheader("1 · Feature engineering & classical models")
st.markdown(
    "- **Combine** `designation` + `description`; keep French/English rows; strip **HTML** (BeautifulSoup) "
    "and **e-mail** noise; tokenize.\n"
    "- **Vectorize** with `TfidfVectorizer`; balance the 27 classes with **SMOTE**.\n"
    "- **Classical baselines** on the TF-IDF matrix: **K-Nearest-Neighbors** and **XGBoost**, both "
    "(tuned with grid / Bayesian search).")
st.caption(f"Source: Rakutan_feature_engineering.py on Jonathan's branch -> {GH}")

st.subheader("2 · Deep learning - XLM-RoBERTa")
st.markdown(
    "- A custom `XLMRoBERTaClassifier` on top of **`xlm-roberta-base`** (`AutoModel.from_pretrained`), "
    "max sequence length 256, dropout 0.3, a linear head over the 27 classes.\n"
    "- Multilingual by design - fits the corpus (~81% French, rest English/German), no per-language model needed.\n"
    "- **HTML cleaned with BeautifulSoup.** Class-weights and several learning-rate schedules were tried; "
    "**none outperformed** the clean BeautifulSoup-based model.\n"
    "- **Best text model: weighted-F1 ≈ 0.87**, well above the text benchmark (0.8113).")
st.caption(f"Source: Rakutan_nn.py on Jonathan's branch -> {GH}")

st.markdown(
    '<div class="rk-win"><b>Hand-off to fusion.</b> This XLM-RoBERTa text representation is the text branch '
    'that Thomas combines with the EfficientNet-B0 image branch to build the multimodal model '
    '(see <b>Merge &amp; comparison</b>).</div>', unsafe_allow_html=True)
footer()
