# Latest V5 — GitHub-to-Overleaf editable recovery (PDF-only source)

This repository now includes a **56-page PDF-to-text LaTeX reconstruction** on main.
It is not the native V5 Overleaf source and NOT a page-identical recreation of the supplied PDF.
The original 56-page PDF remains the authoritative visual reference.

**Use in an Overleaf project linked to this GitHub repo**:
1. In Overleaf: Integrations > GitHub > Pull GitHub changes.
2. Choose **main.tex** at the repository root as the main LaTeX document.
3. Compile using XeLaTeX. The original dated project is preserved under
   `FCS LaTeX Template(1)/`, with `template.tex` unchanged.
4. To display the **exact original V5 PDF without any layout difference**, upload
   `latest_v5.pdf` from the previously delivered
   `MAS_V5_Overleaf_import_exact.zip` to Overleaf and select the archive
   wrapper `V5_PDF_Archive.tex` from that ZIP as main. PDF binary was not
   uploaded by the GitHub connector in this operation.

**Files on main**
- `main.tex`: XeLaTeX root for recovered editable text.
- `V5_RECOVERED/page_01.tex` ... `page_56.tex`: preserved per-page PDF text.
- `v5_experimental_reconciliation.tex`: all author-reported new V5 Tables
  7–11 plus DRICE summary, including explicit statistical caveats.

**Caveats:** figures, float layout, mathematical typesetting, the V5 original
bibliography formatting and page geometry are not natively reconstructed;
some extracted text may need manual restoration. The recovered numerical tables
are marked author-reported and not independently replicated. This update does
not claim 8/10 evidence quality or an Overleaf account-side synchronization.

**Further evidence audit:** see the separate GitHub draft PR #1, which contains
a 60-entry evidence matrix and citation corrections not yet promoted to main.
