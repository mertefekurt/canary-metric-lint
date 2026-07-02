# canary-metric-lint

> Check canary rollout plans for metric, threshold, and rollback gaps.

## Operator guide Overview

Check canary rollout plans for metric, threshold, and rollback gaps. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts canary rollout plan. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
canary-metric-lint examples/sample.txt
canary-metric-lint examples/sample.txt --json --fail-on medium
python -m canary_metric_lint --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-metric` | high | canary metric is missing |
| `missing-threshold` | medium | canary threshold is unclear |
| `unknown-rollback` | low | rollback is unclear |

## Validation Notes

```bash
ruff check .
pytest
python -m canary_metric_lint --help
```

Example risky input:

```text
canary metric missing threshold none rollback unknown
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
