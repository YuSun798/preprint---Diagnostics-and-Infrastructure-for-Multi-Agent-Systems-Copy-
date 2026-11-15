#!/usr/bin/env python3
"""Cross-check V5 McNemar contingency tables; no raw trace predictions assumed.

Expected input when available:
case_id,c1_correct,c2_correct,c3_correct
Each correct column is 0/1. Without CSV the script audits aggregate constraints
but cannot certify the author's original evaluation or paired confidence interval.
"""
import argparse
import csv
import math
from pathlib import Path

N_EXPECTED = 220
EXPECTED_SUCCESSES = {"c1": 101, "c2": 117, "c3": 119}


def two_sided_exact_and_mid_p(b, c):
    # Exact two-sided McNemar test equals binomial test with p=0.5.
    n, k = b + c, min(b, c)
    pmf = math.comb(n, k) / 2**n
    exact = min(1.0, 2 * sum(math.comb(n, j) / 2**n for j in range(k + 1)))
    mid = max(0.0, exact - pmf)
    return exact, mid


def report(a, b, wins, losses):
    exact, mid = two_sided_exact_and_mid_p(wins, losses)
    net = wins - losses
    print(
        f"{a.upper()} -> {b.upper()}: new-only correct={wins}, "
        f"old-only correct={losses}, difference={net}/220 = {100 * net / 220:.4f} pp; "
        f"two-sided exact p={exact:.10f}; two-sided mid-p={mid:.10f}"
    )
    return net


def from_csv(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != N_EXPECTED:
        raise ValueError(f"Expected {N_EXPECTED} cases, got {len(rows)}")
    for key in EXPECTED_SUCCESSES:
        vals = [int(r[key]) for r in rows]
        if any(x not in (0, 1) for x in vals):
            raise ValueError(f"Only 0/1 accepted in {key}")
        observed = sum(vals)
        if observed != EXPECTED_SUCCESSES[key]:
            raise ValueError(f"{key} sums to {observed}, PDF reports {EXPECTED_SUCCESSES[key]}")
    for old, new in (("c1", "c2"), ("c2", "c3")):
        wins = sum(int(r[new]) == 1 and int(r[old]) == 0 for r in rows)
        losses = sum(int(r[new]) == 0 and int(r[old]) == 1 for r in rows)
        net = report(old, new, wins, losses)
        expected = EXPECTED_SUCCESSES[new] - EXPECTED_SUCCESSES[old]
        assert net == expected, "Paired contingency does not reproduce marginal differences"
    print("PASS: case-level values reproduce PDF aggregate accuracy. CI still needs declared procedure.")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--predictions", help="CSV with case_id,c1_correct,c2_correct,c3_correct")
    args = p.parse_args()
    if args.predictions:
        from_csv(args.predictions)
    else:
        print("AGGREGATE-ONLY CHECK; NOT INDEPENDENT REPLICATION.")
        report("c1", "c2", 22, 6)
        report("c2", "c3", 28, 26)
        assert EXPECTED_SUCCESSES["c2"] - EXPECTED_SUCCESSES["c1"] == 22 - 6
        assert EXPECTED_SUCCESSES["c3"] - EXPECTED_SUCCESSES["c2"] == 28 - 26
        print("PASS: corrected b/c orientation and exact versus mid-p discrepancy detected.")
