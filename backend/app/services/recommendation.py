"""
Generate response recommendations.

This service maps attack types
to SOC actions.
"""


def generate_recommendations(alert: dict):

    recommendations = []

    title = alert.get("title", "").lower()
    description = alert.get("description", "").lower()

    # ------------------------
    # SQL Injection
    # ------------------------
    if "sql" in title or "sql" in description:

        recommendations.extend([
            "Inspect database logs.",
            "Block suspicious SQL payloads.",
            "Enable WAF SQL Injection rules.",
            "Review affected database accounts."
        ])

    # ------------------------
    # Malware
    # ------------------------
    elif "malware" in description:

        recommendations.extend([
            "Disconnect infected endpoint.",
            "Run antivirus scan.",
            "Collect malware sample.",
            "Review persistence mechanisms."
        ])

    # ------------------------
    # Login Attack
    # ------------------------
    elif "login" in description:

        recommendations.extend([
            "Reset compromised credentials.",
            "Enable MFA.",
            "Review authentication logs.",
            "Block suspicious IP."
        ])

    # ------------------------
    # Generic
    # ------------------------
    else:

        recommendations.extend([
            "Review logs.",
            "Investigate manually.",
            "Notify SOC analyst."
        ])

    return recommendations