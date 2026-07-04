"""
Workflow Connections

Later we will add conditions here.
"""


def next_after_triage(state):

    return "rag"


def next_after_rag(state):

    return "graph"


def next_after_graph(state):

    return "__end__"