from app.services.LLM import ask_llm


def investigate_alert(alert):

    prompt = f"""

You are SOC Analyst.

Investigate this alert.

Title:
{alert.title}

Description:
{alert.description}

Severity:
{alert.severity}

Return:

1. Summary

2. Root Cause

3. MITRE ATT&CK Technique

4. IOC

5. Recommendation

"""

    return ask_llm(prompt)