"""About — team roles and deliverables (brief)."""
import streamlit as st
from _shared import page, footer

page("About", "ℹ️")
st.title("About")
st.markdown("Liora MLE — Project 06: multimodal product classification on the Rakuten France catalogue.")

st.subheader("Team roles")
st.markdown(
    "- **Sandeep Grover** — business case, data exploration & data-visualization, text pre-processing "
    "(TF-IDF, 80/20 split). *(This app's Data & EDA page + the report.)*\n"
    "- **Jonathan Vints** — machine-learning models (classical → deep learning) and multimodal fusion.\n"
    "- **Thomas Maisch** — image branch (CNN / image model), images only.")

st.subheader("Data")
st.markdown("Rakuten France Multimodal Product Data Classification challenge — `X_train_update.csv` "
            "(designation, description, image ids) and `Y_train_CVw08PX.csv` (`prdtypecode`). "
            "84,916 products (83,502 after removing 1,414 exact duplicates) · 27 classes · imbalance ratio 14.2×.")

st.subheader("Deliverables")
st.markdown("- This interactive **Streamlit app** (the course restitution)\n"
            "- The written **project report** (see the Report page — PDF / Word)")
footer()
