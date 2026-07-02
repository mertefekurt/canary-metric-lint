from __future__ import annotations

from canary_metric_lint.models import Rule

PROJECT_NAME = 'canary-metric-lint'
SUMMARY = 'Check canary rollout plans for metric, threshold, and rollback gaps.'
SAMPLE_RISK = 'canary metric missing threshold none rollback unknown'
SAMPLE_CLEAN = 'canary metric error_rate threshold 2% rollback documented'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='missing-metric',
        severity='high',
        pattern='metric\\s+(missing|none|unknown)',
        message='canary metric is missing',
        recommendation='choose a user-impact metric',
    ),
    Rule(
        code='missing-threshold',
        severity='medium',
        pattern='threshold\\s+(none|missing|unknown)',
        message='canary threshold is unclear',
        recommendation='define stop or rollback threshold',
    ),
    Rule(
        code='unknown-rollback',
        severity='low',
        pattern='rollback\\s+(unknown|missing|none)',
        message='rollback is unclear',
        recommendation='link rollback command or runbook',
    ),
)
