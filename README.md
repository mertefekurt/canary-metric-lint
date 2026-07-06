# Canary Metric Lint

Check canary rollout plans for metric, threshold, and rollback gaps.

## First impression

![Canary Metric Lint cover](assets/readme-cover.svg)

When this tool reports something, I want the finding to be boringly explicit: what matched, how severe it is, and what a reviewer should clean up.

## Tripwires

- `missing-metric` (high): canary metric is missing. Fix: choose a user-impact metric.
- `missing-threshold` (medium): canary threshold is unclear. Fix: define stop or rollback threshold.
- `unknown-rollback` (low): rollback is unclear. Fix: link rollback command or runbook.

## Runbook

```bash
git clone https://github.com/mertefekurt/canary-metric-lint.git
cd canary-metric-lint
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Then:

```bash
canary-metric-lint examples/sample.txt
canary-metric-lint examples/sample.txt --json
```

## Development note

The policy lives in `rules.py`; parsing and rendering stay separate so the rule list is easy to audit.
