"""
Hybrid Retrieval

Combines

1. Keyword Search (BM25)

2. Semantic Search (Qdrant)

Later

↓

Reciprocal Rank Fusion

↓

Cross Encoder Reranking
"""

from app.db.qdrant import search_vectors


def keyword_search(query: str):
    """
    Temporary BM25.

    Later we will replace this with
    Elasticsearch / BM25.
    """

    return [

        "Reset Credentials",

        "Collect Firewall Logs",

        "Block Suspicious IP"

    ]


def reciprocal_rank_fusion(keyword_results, semantic_results):
    """
    Simple Rank Fusion.

    Removes duplicates while preserving order.

    Later:
        Proper RRF Formula
    """

    merged = []

    for result in keyword_results + semantic_results:

        if result not in merged:

            merged.append(result)

    return merged


def hybrid_search(query: str):
    """
    Main Hybrid Retrieval Pipeline
    """

    # Step 1
    keyword_results = keyword_search(query)

    # Step 2
    semantic_results = search_vectors(query)

    # Step 3
    final_results = reciprocal_rank_fusion(

        keyword_results,

        semantic_results

    )

    return final_results