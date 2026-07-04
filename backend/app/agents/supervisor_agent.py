from app.graph.workflow import graph


"""
Supervisor Agent

This is the brain of the SOC.

Responsibilities

1. Run LangGraph

2. Decide which tools to use

3. Return final response
"""

from app.graph.workflow import graph

from app.mcp.registry import TOOLS


def investigate(alert):

    # -----------------------------
    # Initial shared state
    # -----------------------------
    state = {

        "title": alert.title,

        "description": alert.description,

        "severity": alert.severity,

        "classification": "",

        "summary": "",

        "playbook": [],

        "graph_entities": []

    }

    # -----------------------------
    # Execute LangGraph workflow
    # -----------------------------
    result = graph.invoke(state)

    # -----------------------------
    # Example:
    # Automatically block IP
    # if severity is HIGH
    # -----------------------------
    if result["severity"] == "HIGH":

        firewall = TOOLS["firewall"]

        result["action"] = firewall("192.168.1.10")

    return result