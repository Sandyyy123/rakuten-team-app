"""Report - serves the actual project report we created (PDF + DOCX)."""
import os, base64
import streamlit as st
from _shared import page, footer

page("Report", "📄")
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF  = os.path.join(BASE, "downloads", "Rakuten_Project_Report.pdf")
DOCX = os.path.join(BASE, "downloads", "Rakuten_Project_Report.docx")

st.title("Project report")
st.caption("Exploration, data-visualization and pre-processing report - Sandeep Grover · Jonathan Vints · "
           "Thomas Maisch. This is the actual report document (not a re-typed copy).")

c1, c2 = st.columns(2)
with c1:
    with open(PDF, "rb") as f:
        st.download_button("⬇ Download report (PDF)", f.read(),
                           file_name="Rakuten_Project_Report.pdf", mime="application/pdf",
                           use_container_width=True)
with c2:
    with open(DOCX, "rb") as f:
        st.download_button("⬇ Download report (Word .docx)", f.read(),
                           file_name="Rakuten_Project_Report.docx",
                           mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                           use_container_width=True)

st.divider()
st.subheader("Inline preview")
with open(PDF, "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")
st.markdown(
    f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="900" '
    'style="border:1px solid #e2e8f0;border-radius:8px"></iframe>',
    unsafe_allow_html=True,
)
st.caption("If the inline preview does not display in your browser, use the Download button above.")
footer()
