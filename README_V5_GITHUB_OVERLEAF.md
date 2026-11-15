# Diagnostics and Serving Infrastructure for Foundation Model-Based Multi-Agent Systems
## Unified Neurocomputing source — authoritative root: main.tex

The repository's **root main.tex** is now a single Elsevier-style, editable manuscript
reconstructed from the author's 56-page V5 PDF. It is not the old per-page
verbatim dump. The previous LaTeX manuscript is preserved under
`FCS LaTeX Template(1)/` for source history, not imported as a second paper.

### What is integrated
- Ten main numbered sections plus the system census and evidence-audit appendix;
- **All 13 original manuscript tables as native, editable LaTeX longtables**;
- Four figures: Figures 1–3 preserved from the V5 PDF as figure assets and
  Figure 4 rebuilt to use the **same twelve benchmarks** as Table 3 and
  distinguish native step-level root-cause labels from task-success scoring;
- Original **52 bibliography entries** with original numeric citation IDs,
  plus 14 supplemental source records mapped from previously uncited methods;
- Original V5 new retention experiments (Tables 7–11), corrected McNemar pair
  direction, two-sided exact p-value labelling, DRICE and section-level analysis.

### Reproducible compile
From Overleaf: **Integrations → GitHub → Pull GitHub changes** and select
root `main.tex` as the Main document; use **XeLaTeX**. The old
`FCS LaTeX Template(1)/template.tex` must NOT be selected.
Locally run `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex`.
CI builds the article on GitHub and uploads the compiled PDF artifact.

### Content and scientific provenance
- V5 is the **authoritative** current manuscript. The previous 55-page PDF was
  compared, and superseded claims or bibliographic errors were **not** revived.
  The 56-page original PDF and the old PDF are preserved in the downloadable
  unified ZIP artifact supplied in ChatGPT, not embedded in GitHub source.
- Corrected TokenCake EuroSys 2027 ordinal, tau-bench author list, NeurIPS
  2024 proceedings label, and benchmark root-cause capability classification.
- Reported numerical Tables 7–11 are **not new independently reproduced
  experiments**. The raw 220-case correctness vectors and cache access/eviction
  logs were not supplied; paired confidence bounds and cache denominators must
  be independently regenerated before declaring evidence-quality 8/10.
- The 60-entry source tiers are inherited from author V5; bibliography mapping
  is not equivalent to full-text claim-by-claim verification.

The project's GitHub CI validates **compilability and structural completeness**.
It cannot certify every scientific statement or guarantee acceptance.
