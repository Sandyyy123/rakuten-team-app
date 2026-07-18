"""Data & EDA - Sandeep Grover's section. Uses the figures, captions and prose from the
project report (Rakuten_Project_Report)."""
import os
import streamlit as st
from _shared import page, footer, tiles, raku

page("Data & EDA", "📊")
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RF = os.path.join(BASE, "report_figs")
R = raku(); s = R["stats"]

st.title("Data exploration & text pre-processing")
st.caption("Sandeep Grover · Business case, data exploration and text pre-processing (TF-IDF, 80/20 split). "
           "Figures, captions and numbers are taken from the project report.")

# ---- Business case / context ---------------------------------------------------
st.header("1 · Business case")
st.markdown(
    "Cataloguing products from their text and image is a core problem for any e-commerce marketplace: "
    "the correct category drives search, filtering, recommendation and merchandising. On **Rakuten France**, "
    "millions of third-party sellers upload products with a short title (*designation*), an optional free-text "
    "*description*, and a single product image. Assigning each listing to the correct product-type code by "
    "hand does not scale, and seller-supplied labels are unreliable - titles are free-form and multilingual, "
    "many products have no description, and some are mislabelled.")
st.markdown(
    "**Objective.** Predict the product-type code (`prdtypecode`) of each listing from its text and image - "
    "the public Rakuten France Multimodal Product Data Classification challenge [1] (27 product-type codes). "
    "**Team project:** this report covers the business framing, data exploration and text pre-processing; "
    "teammates' work follows - the models and multimodal fusion (Jonathan Vints), and the image branch "
    "(Thomas Maisch).")

tiles([
    (f"{s['n_products']:,}",             "Products"),
    (str(s["n_classes"]),                "Categories"),
    (f"{s['imbalance_ratio']}×",         "Imbalance (max/min class)"),
    (f"{s['pct_missing_description']}%", "Missing description"),
    (f"{s['median_text_len']}",          "Median text length (chars)"),
])
st.divider()

# ---- 2 Exploration: the 5 report figures ---------------------------------------
st.header("2 · Data exploration & visualization")
st.markdown("Every statistical test below exists to justify one concrete pre-processing or modelling decision.")
st.caption("Duplicate analysis: 1,414 exact duplicate listings (1.7%) were found and removed, leaving the "
           "83,502 analysed here (2,651, 3.1%, share a title alone).")

st.subheader("2.1 Class imbalance")
st.markdown("The 27 categories are heavily imbalanced: the largest class holds **9,814** listings and the "
            "smallest **693** - a **14.2-to-1** ratio. A chi-square goodness-of-fit test against a uniform "
            "distribution gives **χ² = 35,282 (p < 0.001)**, so the imbalance is real, not sampling noise. "
            "Because the Rakuten challenge is scored on the **weighted-F1** score, weighted-F1 is the primary "
            "metric; macro-F1 is also tracked. Class weighting and stratified splits are applied.")
st.image(os.path.join(RF, "cxd_classdist.png"), use_container_width=True)
st.caption("Figure 1. Distribution of the 27 product categories, showing the 14.2-to-1 imbalance.")

st.subheader("2.2 Missing descriptions - a Missing-At-Random signal")
st.markdown("**35.5%** of listings have no description, and the missing rate is **not uniform** across "
            "categories. A chi-square test of independence between description present/absent and the class "
            "gives **χ² = 42,953** and **Cramér's V = 0.72** (p < 0.001) - a strong association. Because the "
            "absence depends on the **observed** category, the missingness is **Missing At Random (MAR)** "
            "(not MNAR, which would require dependence on the unobserved text itself): its presence is "
            "informative. Rather than dropping ~35% of the data, a binary `desc_missing` indicator is added "
            "so the model can use the absence as a feature.")
st.image(os.path.join(RF, "cxd_missing.png"), use_container_width=True)
st.caption("Figure 2. Missing-description rate per category, showing a strong category dependence (Missing At Random).")

st.subheader("2.3 Text length varies by category")
st.markdown("Total text length (title + description) is heavily right-skewed. Because the distribution is "
            "skewed, a non-parametric **Kruskal-Wallis** test is used instead of a normal ANOVA; it confirms "
            "length differs significantly across categories (p < 0.001). Designation and description lengths "
            "are retained as numeric features.")
st.image(os.path.join(RF, "cxd_textlen.png"), use_container_width=True)
st.caption("Figure 3. Distribution of text length per listing, with the median marked; note the heavy right tail.")

st.subheader("2.4 Language distribution")
st.markdown("The text is predominantly French but contains a genuine English and German tail. **Wilson 95% "
            "confidence intervals**, which remain valid for the rare languages where the normal approximation "
            "breaks down, confirm that English and German are real sub-populations, not noise. This favours a "
            "French/multilingual model in the modelling stage - **CamemBERT** (a French RoBERTa), FlauBERT or XLM-R.")
st.image(os.path.join(RF, "cxd_lang.png"), use_container_width=True)
st.caption("Figure 4. Language distribution across listings: predominantly French, with an English and German tail.")

st.subheader("2.5 Word frequency")
st.markdown("**Top panel (raw counts):** the most frequent words are almost all stopwords (*de, la, et, "
            "pour, les*) - they carry no category signal and are **removed with the nltk FR/EN/DE stopword lists**. "
            "**Bottom panel (after removal):** the most frequent remaining content words are real, unstemmed terms "
            "(*cm, couleur, taille, piscine, eau*) - exactly the discriminative features TF-IDF keeps. The rarest "
            "terms (one-off typos/serials) are dropped by the minimum-document-frequency threshold and the "
            "20,000-feature cap.")
st.image(os.path.join(RF, "cxd_wordfreq.png"), use_container_width=True)
st.caption("Figure 5. Word frequency before vs after stopword removal. Top: raw counts are dominated by "
           "stopwords (removed). Bottom: the surviving most frequent tokens are content words.")
st.divider()

# ---- 3 Pre-processing ----------------------------------------------------------
st.header("3 · Pre-processing & feature engineering")
st.subheader("3.1 Text cleaning (per listing, before the split)")
st.markdown("These operations act on each listing independently, so they carry no information between rows and "
            "are applied to the whole dataset **before** splitting: designation + description **merged into one "
            "field** and lowercased; URLs, e-mails, HTML tags and entities (stripped by **regex**, so "
            "`rouge<br>bleu` becomes `rouge bleu`), sizes and numbers are stripped while **French accents are "
            "kept**; the text is tokenised with **TweetTokenizer**, **FR/EN/DE stopwords are removed (nltk)** and "
            "one-character tokens dropped (**no stemming**). The transformer branch instead uses a near-raw copy "
            "(`text_nostem`) that keeps stopwords; a binary `desc_missing` indicator is built before any fill.")
st.subheader("3.2 Train / test split")
st.markdown("The data are split **80/20**, **stratified on `prdtypecode`** so both sets preserve the 27-class "
            "proportions. The test set is held out purely for evaluation. Any transformation that learns from "
            "the corpus is fitted on the **training set only**, to avoid data leakage.")
st.subheader("3.3 TF-IDF vectorization")
st.markdown("TF-IDF (scikit-learn) turns each merged text into a numeric vector: term frequency × inverse "
            "document frequency (log of N over the number of documents containing the term). **Stopwords "
            "(*de, le, et*) are already removed, so they are never columns**; among the remaining content words, "
            "common ones get a lower weight via IDF - e.g. *couleur* (18,030 docs → IDF 2.5) vs "
            "*nintendo* (825 docs → IDF 5.6). Both **unigrams and bigrams** are used -  *jeux video* is a "
            "strong marker that neither *jeux* nor *video* conveys alone - and the vocabulary is capped at the "
            "**20,000** most useful terms out of ~280,000.")
st.markdown("The result is a **sparse matrix** - rows = listings, columns = 20,000 terms, each cell a TF-IDF "
            "score, ~99% zeros. Fitted on train only, then applied to both sets. The deliverable handed to the "
            "modelling stage is **~66,800 train / ~16,700 test** rows: 20,000 sparse TF-IDF features plus "
            "`desc_missing` and length features, over the 27 target categories.")
st.markdown('<div class="rk-win"><b>Hand-off:</b> the numeric feature matrix goes to Jonathan Vints '
            '(models + multimodal fusion) and Thomas Maisch (image branch).</div>', unsafe_allow_html=True)
footer()
