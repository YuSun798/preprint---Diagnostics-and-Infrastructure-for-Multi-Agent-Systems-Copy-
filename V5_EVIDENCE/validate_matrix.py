#!/usr/bin/env python3
"""CI structural checks for V5 evidence matrix and bibliography additions.

Checks presence/completeness, not scholarly accuracy of source claims.
"""
import csv
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
matrix = ROOT / "evidence_matrix_60.csv"
bib = ROOT.parent / "FCS LaTeX Template(1)" / "v5_primary_sources.bib"

with matrix.open(newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 60, f"Expected 60 core entries; got {len(rows)}"
assert {int(r["row"]) for r in rows} == set(range(1, 61))
counts = {}
for r in rows:
    counts[r["category"]] = counts.get(r["category"], 0) + 1
assert counts == {
    "Failure-Loc": 12, "Observability": 6,
    "Safety": 8, "Infrastructure": 22, "Benchmark": 12
}, counts
assert all(r["claimed_tier_in_V5"] in {"T1a","T1b","T2"} for r in rows)
assert len([r for r in rows if r["claimed_tier_in_V5"] == "T2"]) == 4
assert all(r["fulltext_section_table_verified_by_this_audit"] == "PENDING" for r in rows), (
    "Only mark full-text evidence as verified after actual paper-level verification."
)
bibkeys = re.findall(r"@\w+\{\s*([^,\s]+)", bib.read_text(encoding="utf8"))
assert len(bibkeys) >= 15
assert len(set(bibkeys)) == len(bibkeys)
source_bytes = sum(p.stat().st_size for p in (ROOT.parent / "V5_SOURCE_SNAPSHOT").glob("pages_*.txt"))
assert source_bytes > 150000, "V5 PDF transcription is missing pages or too short"
print("PASS: 60-item census, 56/4 tier pattern, 12 benchmark labels, "
      f"{len(bibkeys)} new source records, V5 text snapshot ({source_bytes} bytes).")
print("NOTE: This checks STRUCTURE ONLY, NOT primary-text verification or experiments.")
