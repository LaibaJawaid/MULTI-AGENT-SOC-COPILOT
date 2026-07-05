"""
Threat Intelligence Agent

Collects MITRE, IOC and CVE information.
"""

from app.services.mitre import get_mitre
from app.services.ioc import extract_iocs
from app.services.cve import get_related_cves


def analyze_threat(alert: dict):

    description = alert.get("description", "")

    return {

        # MITRE Mapping
        "mitre": get_mitre(alert),

        # IOC Extraction
        "ioc": extract_iocs(description),

        # Related CVEs
        "cves": get_related_cves(alert)

    }