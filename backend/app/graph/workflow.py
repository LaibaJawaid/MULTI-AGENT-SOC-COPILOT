"""
Main LangGraph Workflow
"""

from langgraph.graph import StateGraph
from langgraph.graph import END

from app.graph.state import InvestigationState

from app.graph.nodes import (
    triage_node,
    rag_node,
    graph_node
)

builder = StateGraph(InvestigationState)

builder.add_node("triage", triage_node)

builder.add_node("rag", rag_node)

builder.add_node("graph", graph_node)

builder.set_entry_point("triage")

builder.add_edge("triage", "rag")

builder.add_edge("rag", "graph")

builder.add_edge("graph", END)

graph = builder.compile()