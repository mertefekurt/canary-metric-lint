<p align="center">
  <img src="assets/readme-cover.svg" alt="Canary Metric Lint cover" width="100%" />
</p>

# Canary Metric Lint

![stack](https://img.shields.io/badge/stack-Python-0891b2?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-b45309?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-be185d?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-4b5563?style=flat-square)

Check canary rollout plans for metric, threshold, and rollback gaps.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `canary-metric-lint` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
canary-metric-lint examples/sample.txt
canary-metric-lint examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-metric` | high | canary metric is missing |
| `missing-threshold` | medium | canary threshold is unclear |
| `unknown-rollback` | low | rollback is unclear |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
canary metric missing threshold none rollback unknown
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m canary_metric_lint --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Canary Metric Lint policy easy to review.
