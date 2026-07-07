"""
Threat Intelligence Service

Responsible for:

1. VirusTotal Lookup

2. AbuseIPDB Lookup

3. MITRE Mapping

Currently returns mock data.

Later Sprint 22
real APIs will be integrated.
"""

from typing import Dict
from app.services.ioc_extractor import extract_iocs


def lookup_threat(alert: Dict):

    iocs = extract_iocs(alert["description"])

    description = alert["description"].lower()

    # -------------------------
    # Fake Threat Intelligence
    # -------------------------

    if "powershell" in description:

        return {

            "iocs": iocs,

            "ioc_type": "PowerShell",

            "mitre": "T1059.001",

            "attack_name": "PowerShell",

            "abuse_score": 92,

            "malicious": True

        }

    if "sql" in description:

        return {

            "ioc_type": "SQL",

            "mitre": "T1190",

            "attack_name": "Exploit Public Facing Application",

            "abuse_score": 70,

            "malicious": True

        }

    return {

        "ioc_type": "Unknown",

        "mitre": "N/A",

        "attack_name": "Unknown",

        "abuse_score": 0,

        "malicious": False

    }