# Integration status — V5 evidence upgrade (2026-11-12)

## IMPORTANT: This is not yet a full, lossless V5 Overleaf migration
Authoritative source supplied in this conversation: 56-page PDF
"Survey_MAS_Diagnostics_Neurocomputing_v5_evidence_audit(1).pdf".
GitHub main initially contained a significantly older LaTeX revision (Nov. 7),
not the source for this 56-page PDF. The native editable V5 LaTeX .tex files,
current figures, bibliography, and original experiment logs were not provided.
Therefore there is **no defensible guarantee that PDF-to-LaTeX conversion
could preserve the complete V5 manuscript**.

The upgrade branch does **not overwrite** the old manuscript. It:
- Preserves all **56 pages' extracted textual content**, including the PDF's
  new DRICE and experiment sections, in 7 numbered V5_SOURCE_SNAPSHOT files.
  They are text evidence, not editable LaTeX or restored diagrams.
- Reintroduces **Tables 7–11** in structured LaTeX
  (\`FCS LaTeX Template(1)/v5_experimental_reconciliation.tex\`),
  with original numbers and transparent flags for non-reproducibility.
  This file is included from the older main \`template.tex\` on this branch.
- Adds a 60-row V5_EVIDENCE/evidence_matrix_60.csv; all uninspected full-text
  references explicitly remain PENDING, even when V5 claims T1a.
- Adds 15 primary-source bibliographic records (14 missing V5 entries plus
  tau-bench) in \`FCS LaTeX Template(1)/v5_primary_sources.bib\`.
- Corrects legacy LaTeX benchmark labels, FAMAS/TrajAudit figures and
  the McNemar test's descriptive statistical language.
- Adds tests for 60-row structural completeness and aggregate paired-test math.

## The user-requested 8/10 evidence target: criteria, not an invented status
The original V5 was previously rated around 6/10 on evidence rigor. Updating
bibliography metadata and adding an evidence matrix does NOT independently
validate all primary text, which remains a prerequisite for a credible 8/10:
1. Verify all 60 primary sources, with original title/DOI/arXiv/URL; identify
   standards/vendor sources separately from peer-reviewed papers.
2. For each numerical or mechanism claim, extract exact source section/table/
   page and metric denominator, then have a second independent checker confirm.
3. Repair all T2 fine-grained claims: StepFinder, FALAT, DoVer and VerifyMAS.
4. Correct all 12 benchmark capabilities by native (not inferred) labels.
5. Reproduce Table 11 from per-case predictions, not summary numbers.
6. Reproduce Tables 7/8 from event logs, including cache-hit/eviction semantics.
7. Publish scripts with environment lock and trace dataset access instructions.
8. Compile **native V5** LaTeX with complete diagrams, verifying all 56
   manuscript pages/figures/tables and correcting any genuine source changes.

See \`V5_EVIDENCE/REVIEW_GATES.md\` for details; the editorial score should only
be reconsidered when these checks are complete. No guarantee of journal
acceptance or numeric evaluation score is possible.

## To complete an exact editable V5 sync
1. In the Overleaf project **currently containing V5**, use Menu -> Download ->
   Source to export a ZIP (or Git clone the Overleaf project if available).
2. Provide this ZIP, including the latest .tex/.bib/figures and experiment
   scripts or datasets (if separate). Exported PDF alone is not enough.
3. Merge its *native files* into this repository in a dedicated branch; run
   full-reference verification and lossless manuscript diff before merging
   into main. Avoid importing old \`template.tex\` over newer Overleaf V5.
4. Once the completed branch is merged into GitHub \`main\`, open Overleaf
   -> Integrations -> GitHub -> Pull GitHub changes. GitHub-to-Overleaf is
   not automatic, and this connector has no access to the Overleaf account.

Current migration state: **GitHub revision branch updated; main not
replaced; Overleaf not synchronized; evidence 8/10 gate NOT passed.**
