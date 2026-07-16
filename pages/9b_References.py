"""References - verified bibliography for the Rakuten multimodal project."""
import html, re
import streamlit as st
from _shared import page, footer, CORAL, INK, MUTED

page("References", "📚")

# Verified sources, numbered in first-citation order (Vancouver style).
# Every entry confirmed against CrossRef or the authoritative source.
REFS = [
    "Amoualian, H., Goswami, P., Das, P., Montalvo, P., Ach, L., Dean, N.R. (2021). An E-Commerce "
    "Dataset in French for Multi-modal Product Categorization and Cross-Modal Retrieval. Advances in "
    "Information Retrieval (ECIR 2021), LNCS 12657, 18-31. Springer. DOI:10.1007/978-3-030-72113-8_2.",

    "Pearson, K. (1900). On the criterion that a given system of deviations from the probable in the "
    "case of a correlated system of variables is such that it can be reasonably supposed to have arisen "
    "from random sampling. Philosophical Magazine, 50(302), 157-175. DOI:10.1080/14786440009463897.",

    "Cramer, H. (1946). Mathematical Methods of Statistics. Princeton University Press.",

    "Little, R.J.A., Rubin, D.B. (2019). Statistical Analysis with Missing Data (3rd ed.). Wiley. "
    "DOI:10.1002/9781119482260.",

    "Kruskal, W.H., Wallis, W.A. (1952). Use of Ranks in One-Criterion Variance Analysis. Journal of "
    "the American Statistical Association, 47(260), 583-621. DOI:10.1080/01621459.1952.10483441.",

    "Wilson, E.B. (1927). Probable Inference, the Law of Succession, and Statistical Inference. Journal "
    "of the American Statistical Association, 22(158), 209-212. DOI:10.1080/01621459.1927.10502953.",

    "Martin, L., et al. (2020). CamemBERT: a Tasty French Language Model. Proceedings of ACL 2020, "
    "7203-7219. DOI:10.18653/v1/2020.acl-main.645.",

    "Le, H., et al. (2020). FlauBERT: Unsupervised Language Model Pre-training for French. Proceedings "
    "of LREC 2020, 2479-2490.",

    "Conneau, A., et al. (2020). Unsupervised Cross-lingual Representation Learning at Scale (XLM-R). "
    "Proceedings of ACL 2020, 8440-8451. DOI:10.18653/v1/2020.acl-main.747.",

    "Sparck Jones, K. (1972). A Statistical Interpretation of Term Specificity and Its Application in "
    "Retrieval. Journal of Documentation, 28(1), 11-21. DOI:10.1108/eb026526.",

    "Richardson, L. (2007). Beautiful Soup. crummy.com/software/BeautifulSoup.",

    "Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine "
    "Learning Research, 12, 2825-2830.",

    "Deerwester, S., et al. (1990). Indexing by Latent Semantic Analysis. Journal of the American "
    "Society for Information Science, 41(6), 391-407. "
    "DOI:10.1002/(SICI)1097-4571(199009)41:6<391::AID-ASI1>3.0.CO;2-9.",

    "Cover, T., Hart, P. (1967). Nearest Neighbor Pattern Classification. IEEE Transactions on "
    "Information Theory, 13(1), 21-27. DOI:10.1109/TIT.1967.1053964.",

    "Chawla, N.V., et al. (2002). SMOTE: Synthetic Minority Over-sampling Technique. Journal of "
    "Artificial Intelligence Research, 16, 321-357. DOI:10.1613/jair.953.",

    "Chen, T., Guestrin, C. (2016). XGBoost: A Scalable Tree Boosting System. Proceedings of KDD 2016, "
    "785-794. DOI:10.1145/2939672.2939785.",

    "Liu, Y., et al. (2019). RoBERTa: A Robustly Optimized BERT Pretraining Approach. arXiv:1907.11692.",

    "Wolf, T., et al. (2020). Transformers: State-of-the-Art Natural Language Processing. Proceedings "
    "of EMNLP 2020: System Demonstrations, 38-45. DOI:10.18653/v1/2020.emnlp-demos.6.",

    "Loshchilov, I., Hutter, F. (2019). Decoupled Weight Decay Regularization (AdamW). International "
    "Conference on Learning Representations (ICLR) 2019.",

    "Lundberg, S.M., Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions (SHAP). "
    "Advances in Neural Information Processing Systems 30, 4765-4774.",

    "Tan, M., Le, Q. (2019). EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. "
    "Proceedings of ICML 2019, PMLR 97, 6105-6114.",

    "He, K., et al. (2016). Deep Residual Learning for Image Recognition (ResNet). Proceedings of CVPR "
    "2016, 770-778. DOI:10.1109/CVPR.2016.90.",

    "Kingma, D.P., Ba, J. (2015). Adam: A Method for Stochastic Optimization. International Conference "
    "on Learning Representations (ICLR) 2015.",

    "Selvaraju, R.R., et al. (2017). Grad-CAM: Visual Explanations from Deep Networks via Gradient-based "
    "Localization. Proceedings of ICCV 2017, 618-626. DOI:10.1109/ICCV.2017.74.",
]


def linkify(raw):
    """HTML-escape a reference and turn its DOI / arXiv / URL identifier into a working link."""
    s = html.escape(raw)

    # arXiv id -> arxiv.org/abs
    s = re.sub(r'arXiv:(\d{4}\.\d{4,5})',
               r'arXiv:<a href="https://arxiv.org/abs/\1" target="_blank" rel="noopener">\1</a>', s)

    # DOI -> doi.org (skip DOIs that contain an escaped angle bracket, e.g. the LSA record)
    def _doi(m):
        doi, tail = m.group(1), m.group(2)
        if "&lt;" in doi or "&gt;" in doi or "&amp;" in doi:
            return m.group(0)
        return (f'DOI:<a href="https://doi.org/{doi}" target="_blank" rel="noopener">{doi}</a>{tail}')
    s = re.sub(r'DOI:(10\.\S+?)(\.?)(?=\s|$)', _doi, s)

    # bare Beautiful Soup URL
    s = re.sub(r'(?<![\w./])(crummy\.com/\S+?)(\.?)(?=\s|$)',
               r'<a href="https://\1" target="_blank" rel="noopener">\1</a>\2', s)
    return s


st.title("References")
st.caption(f"Verified bibliography ({len(REFS)} sources) for the data, statistics, text and image "
           "methods used in this project. Numbered in first-citation order (Vancouver style); every "
           "entry confirmed against CrossRef or the authoritative source. DOI, arXiv and URL identifiers "
           "link to the source.")

rows = "".join(
    f'<li><span class="rn">[{i}]</span><span class="rt">{linkify(r)}</span></li>'
    for i, r in enumerate(REFS, 1)
)
st.markdown(
    f"""
    <style>
      ol.reflist {{ list-style:none; margin:8px 0 0; padding:0; counter-reset:none; }}
      ol.reflist li {{ display:flex; gap:12px; padding:11px 4px 11px 2px;
          border-bottom:1px solid #EFE9E6; font-size:.92rem; line-height:1.5; color:{INK}; }}
      ol.reflist li:last-child {{ border-bottom:none; }}
      ol.reflist .rn {{ flex:0 0 auto; min-width:34px; font-weight:800; color:{CORAL}; }}
      ol.reflist .rt {{ flex:1 1 auto; }}
      ol.reflist a {{ color:{CORAL}; text-decoration:none; border-bottom:1px dotted {CORAL}; word-break:break-word; }}
      ol.reflist a:hover {{ text-decoration:none; border-bottom-style:solid; }}
    </style>
    <ol class="reflist">{rows}</ol>
    """,
    unsafe_allow_html=True,
)
footer()
