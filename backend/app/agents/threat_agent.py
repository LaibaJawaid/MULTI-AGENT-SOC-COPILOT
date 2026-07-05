"""
Threat Intelligence Agent

Collects external intelligence
about the alert.

Stores results inside workflow state.
"""

from app.services.threat_intel import lookup_threat


def analyze_threat(state):

    alert = {

        "description": state["description"]

    }

    intelligence = lookup_threat(alert)

    # Save into workflow state
    state["threat_intel"] = intelligence

    return state