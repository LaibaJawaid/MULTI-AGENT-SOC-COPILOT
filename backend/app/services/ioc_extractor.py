"""
IOC Extractor

Responsible for extracting:

1. IP Addresses
2. URLs
3. Domains
4. SHA256 hashes

This module is reusable by every agent.
"""

import re


def extract_iocs(text: str):

    # -----------------------------
    # IP Addresses
    # -----------------------------
    ips = re.findall(
        r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
        text
    )

    # -----------------------------
    # URLs
    # -----------------------------
    urls = re.findall(
        r"https?://[^\s]+",
        text
    )

    # -----------------------------
    # Domains
    # -----------------------------
    domains = re.findall(
        r"\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
        text
    )

    # -----------------------------
    # SHA256 Hash
    # -----------------------------
    hashes = re.findall(
        r"\b[a-fA-F0-9]{64}\b",
        text
    )

    return {

        "ips": list(set(ips)),

        "urls": list(set(urls)),

        "domains": list(set(domains)),

        "hashes": list(set(hashes))

    }