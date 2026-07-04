"""
AI Triage Agent

Responsible for deciding
how urgent an alert is.
"""

from app.services.severity import calculate_severity


def triage(alert: dict):
    """
    Decide alert priority.

    Returns:
        LOW
        MEDIUM
        HIGH
        CRITICAL
    """

    severity = calculate_severity(alert)

    if severity == "CRITICAL":
        action = "INVESTIGATE"

    elif severity == "HIGH":
        action = "INVESTIGATE"

    elif severity == "MEDIUM":
        action = "REVIEW"

    else:
        action = "LOG"

    return {
        "severity": severity,
        "action": action
    }