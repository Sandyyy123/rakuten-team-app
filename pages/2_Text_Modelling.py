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

st.markdown(
    '<div class="rk-note"><b>Preprocessing: shared vs per-model.</b> Row-level steps are the same for every '
    'model, so all models see the same rows: merge title + description, strip HTML (BeautifulSoup), URLs and '
    'e-mails, remove the 1,414 exact duplicates, one stratified 80/20 split. Only the <b>representation</b> '
    'differs, because each architecture needs different input.</div>', unsafe_allow_html=True)
st.markdown(
    "| Step | Classical (KNN/XGBoost) | Transformer (XLM-RoBERTa) |\n|---|---|---|\n"
    "| Lowercase | yes | **no** |\n| Remove stopwords | yes (FR/EN/DE) | **no** |\n"
    "| Fold accents | **no** (lexical in French) | **no** |\n"
    "| Stemming | yes (`text`) | **no** (`text_nostem`) |\n"
    "| Tokenizer | TweetTokenizer | **model's own SentencePiece** |\n"
    "| Vectorisation | TF-IDF 20k -> SVD -> SMOTE | none, the model embeds |\n")
st.caption("Why opposite: TF-IDF only counts tokens, so stopwords are noise and Housse/housse would split one "
           "signal in two. A transformer was pretrained on running text and uses word order and function words, "
           "so the same stripping destroys signal. Measured: 0.87 light cleaning vs 0.82 heavy.")

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
    "- `XLMRoBERTaClassifier` on **`xlm-roberta-base`**: **embeddings frozen, all 12 encoder layers trainable** "
    "(`FREEZE_LAYERS = 0`); head = dropout 0.3 + Linear 768 to 27 over the CLS token.\n"
    "- **`MAX_LEN = 256`** because about **79% of texts fit** under it; 512 mostly adds padding.\n"
    "- Multilingual by design - fits the corpus (~81% French, rest English/German), no per-language model needed.\n"
    "- AdamW lr 2e-5, batch 16, grad-clip 1.0, up to 10 epochs, **ReduceLROnPlateau** (factor 0.5, patience 1), "
    "early stopping (patience 3, min_delta 1e-4) **restoring the best checkpoint**.\n"
    "- **Cleaning is the lever:** light cleaning (BeautifulSoup for HTML + regex for URLs/emails only) gives **0.87**; "
    "heavy cleaning only **0.82**. Stopwords are KEPT: the transformer was pretrained on running text and needs it for context.\n"
    "- Tried without gain: class weights; designation/description as a **sentence pair**; linear-decay schedule.\n"
    "- **Best text model: weighted-F1 = 0.87**, well above the text benchmark (0.8113).")
st.caption(f"Source: Rakutan_nn.py on Jonathan's branch -> {GH}")

st.markdown(
    '<div class="rk-win"><b>Hand-off to fusion.</b> This XLM-RoBERTa text representation is the text branch '
    'that Thomas combines with the EfficientNet-B0 image branch to build the multimodal model '
    '(see <b>Merge &amp; comparison</b>).</div>', unsafe_allow_html=True)
footer()
