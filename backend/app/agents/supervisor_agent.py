from app.agents.soc_agent import process_alert

from app.rag.hybrid_search import hybrid_search

from app.db.neo4j import search_iocs


def investigate(alert):

    # Step 1
    result = process_alert(alert)

    # Step 2
    playbook = hybrid_search(result["summary"])

    # Step 3
    graph = search_iocs(result["summary"])

    return {

        "classification": result["classification"],

        "severity": result["severity"],

        "summary": result["summary"],

        "playbook": playbook,

        "graph_entities": graph

    }