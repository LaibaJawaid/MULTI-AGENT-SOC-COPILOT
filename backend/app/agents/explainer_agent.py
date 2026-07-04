"""
Explain AI decisions.
"""

from app.services.reasoning import build_reasoning
from app.services.confidence import confidence_score


def explain(alert):

    reasons = build_reasoning(alert)

    confidence = confidence_score(reasons)

    return {
        "reasons": reasons,
        "confidence": confidence
    }