"""
Generate reasoning behind AI decisions.
"""


def build_reasoning(alert: dict):

    reasons = []

    title = alert.get("title", "").lower()

    description = alert.get("description", "").lower()

    if "sql" in title or "sql" in description:
        reasons.append("SQL related attack detected.")

    if "login" in description:
        reasons.append("Authentication event observed.")

    if "malware" in description:
        reasons.append("Malware indicators found.")

    if not reasons:
        reasons.append("Matched generic security pattern.")

    return reasons