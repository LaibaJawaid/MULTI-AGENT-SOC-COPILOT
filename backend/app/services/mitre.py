"""
MITRE ATT&CK Mapping Service

Maps alerts to MITRE techniques.
"""


def get_mitre(alert: dict):

    title = alert.get("title", "").lower()
    description = alert.get("description", "").lower()

    # SQL Injection
    if "sql" in title or "sql" in description:

        return {
            "technique": "T1190",
            "name": "Exploit Public-Facing Application",
            "tactic": "Initial Access"
        }

    # Malware
    if "malware" in description:

        return {
            "technique": "T1204",
            "name": "User Execution",
            "tactic": "Execution"
        }

    # Login Attack
    if "login" in description:

        return {
            "technique": "T1110",
            "name": "Brute Force",
            "tactic": "Credential Access"
        }

    # Default
    return {
        "technique": "Unknown",
        "name": "Unknown",
        "tactic": "Unknown"
    }