"""
IOC Extraction Service

Extracts Indicators of Compromise.
"""

import re


def extract_iocs(text: str):

    # -------------------------
    # Extract IP addresses
    # -------------------------
    ips = re.findall(
        r"(?:\d{1,3}\.){3}\d{1,3}",
        text
    )

    # -------------------------
    # Extract domains
    # -------------------------
    domains = re.findall(
        r"[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        text
    )

    return {
        "ips": list(set(ips)),
        "domains": list(set(domains))
    }