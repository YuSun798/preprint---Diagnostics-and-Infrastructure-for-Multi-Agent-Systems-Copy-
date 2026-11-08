# Neurocomputing submission version

Main LaTeX file: **FCS LaTeX Template(1)/template.tex**

The original project folder name is intentionally unchanged, so a previously linked Overleaf project can pull the updated main branch. The manuscript now uses Elsevier elsarticle with numeric citations, revised sections and five replacement vector diagrams.

- Previous FCS version is preserved on branch **backup-fcs-before-neurocomputing-2026-11-07**.
- Overleaf GitHub synchronization is manual. In the already linked Overleaf project, select **Integrations > GitHub > Pull GitHub changes**, then designate **template.tex** as the main file and recompile. Pushing first could overwrite newer GitHub changes if both sides have diverged.
- The main file inputs abstract.tex, introduction.tex, background.tex, diagnostics.tex, infrastructure.tex, tension.tex, discussion.tex, conclusion.tex and the new TikZ figure files from the same project directory.
- Original PNGs and SVG source art are preserved in the repository but are no longer referenced in the revised main figures.
- The evidence audit is at repository root in **EVIDENCE_AUDIT.md**. It lists full-text validation and remaining compilation tasks; **no new empirical results have been invented**.
- The repository changes alone do not establish that any existing Overleaf project has already been synchronized.

See: https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions

For an Elsevier Editorial Manager LaTeX upload, confirm the current journal requirements. Elsevier warns that source-processing uploads may need a flat directory, with text, bibliography and graphics at a single folder level.