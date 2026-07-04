"""
LangGraph Nodes

Each function represents one AI Agent.
"""

from app.agents.soc_agent import analyze_alert
from app.rag.hybrid_search import hybrid_search
from app.db.neo4j import search_iocs


def triage_node(state):

    result = analyze_alert(state)

    state["classification"] = result["classification"]

    state["summary"] = result["summary"]

    return state


def rag_node(state):

    state["playbook"] = hybrid_search(
        state["summary"]
    )

    return state


def graph_node(state):

    state["graph_entities"] = search_iocs(
        state["summary"]
    )

    return state