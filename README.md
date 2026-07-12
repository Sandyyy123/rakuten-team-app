# Rakuten France — Multimodal Product Classification (Team app)

Liora MLE · Project 06. Interactive Streamlit restitution for the Rakuten France multimodal
product-classification challenge (27 `prdtypecode` categories, 84,916 products).

## Team & page ownership

Each project stage is a **separate file** — edit only your own page.

| Page (file) | Owner | Status |
|---|---|---|
| `Home.py` | shared | landing |
| `pages/1_Data_and_EDA.py` | **Sandeep Grover** | ✅ complete (business case, EDA, TF-IDF pre-processing) |
| `pages/2_Modelling_and_Fusion.py` | **Jonathan Vints** | 🚧 placeholder — classical & deep-learning models + multimodal fusion |
| `pages/3_Image.py` | **Thomas Maisch** | 🚧 placeholder — image branch (CNN), images only |
| `pages/4_Demo.py` | team | 🚧 placeholder — live prediction once models exist |
| `pages/5_Report.py` | shared | ✅ serves the project report (PDF / Word) |
| `pages/6_Presentation.py` | shared | ✅ Sandeep's slide deck (embedded) |
| `pages/7_About.py` | shared | team roles |

## How to edit your part

1. You will be added as a **collaborator** on this GitHub repo.
2. Open your page file (Jonathan → `pages/2_Modelling_and_Fusion.py`, Thomas → `pages/3_Image.py`) —
   edit it directly in the GitHub web editor (pencil icon), or clone the repo and edit locally.
3. Commit / push. The live app **auto-redeploys** (Streamlit Community Cloud).

Only change your own page. Shared helpers live in `_shared.py` (colours, `page()`, `footer()`,
`tiles()`, and the data loaders `raku()` / `classes()`).

## Run locally

```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Data / figures

- `data/raku.json`, `data/raku_classes.json` — canonical numbers (traceable to the result files).
- `report_figs/` — the exploration figures used in the written report.
- `downloads/` — the project report (PDF + Word).
