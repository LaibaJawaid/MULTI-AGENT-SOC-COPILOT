"""
Recommendation Agent

Uses:

1. Alert summary

2. Similar incidents

3. Asset graph

Then asks GPT
for final recommendations.
"""

from app.services.LLM import ask_llm


def generate_recommendations(state):

    summary = state["summary"]

    rag = state["rag_results"]

    graph = state["graph_context"]

    threat = state["threat_intel"]

    prompt = f"""
You are an expert SOC analyst.

Alert Summary:

{summary}

Similar Incidents:

{rag}

Infrastructure Context:

{graph}

Threat Intelligence

MITRE Technique:
{threat["mitre"]}

Attack Name:
{threat["attack_name"]}

Abuse Score:
{threat["abuse_score"]}

Malicious:
{threat["malicious"]}

Generate:

1. Root Cause

2. Investigation Steps

3. Containment

4. Recovery

5. Future Prevention

Return concise bullet points.
"""

    recommendations = ask_llm(prompt)

    state["recommendations"] = recommendations

    return state