"""
Threat Intelligence Agent

Collects intelligence
and IOC information.
"""

from app.services.threat_intel import lookup_threat


def analyze_threat(state):

    alert = {

        "description": state["description"]

    }

    intelligence = lookup_threat(alert)

    # Save complete threat intelligence
    state["threat_intel"] = intelligence

    # Save IOC list separately
    state["iocs"] = intelligence["iocs"]

    return state