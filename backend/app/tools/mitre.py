"""
MITRE ATT&CK Tool

Maps attack names to ATT&CK techniques.
"""


def lookup_attack(alert: str):

    text = alert.lower()

    if "powershell" in text:

        return {

            "technique": "T1059.001",

            "name": "PowerShell"

        }

    if "sql" in text:

        return {

            "technique": "T1190",

            "name": "Exploit Public Facing Application"

        }

    return {

        "technique": "Unknown",

        "name": "Unknown"

    }