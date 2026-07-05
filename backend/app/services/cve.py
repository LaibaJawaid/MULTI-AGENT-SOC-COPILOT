"""
CVE Mapping Service

Temporary mock database.
"""


def get_related_cves(alert: dict):

    description = alert.get("description", "").lower()

    if "sql" in description:

        return [
            "CVE-2021-44228",
            "CVE-2023-34362"
        ]

    if "malware" in description:

        return [
            "CVE-2022-30190"
        ]

    return []