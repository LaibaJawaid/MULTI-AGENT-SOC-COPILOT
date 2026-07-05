"""
LangGraph State

Every node reads and writes this object.

Think of it as the memory shared
between all agents.
"""

from typing import TypedDict


class InvestigationState(TypedDict):

    title: str

    description: str

    severity: str

    classification: str

    summary: str

    playbook: list

    graph_entities: list

        # Threat Intelligence
    threat_intel: dict