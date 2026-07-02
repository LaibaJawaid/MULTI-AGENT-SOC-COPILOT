def recommend_action(category: str):

    category = category.lower()

    if category == "sql injection":
        return [
            "Block malicious IP",
            "Validate SQL queries",
            "Use parameterized statements"
        ]

    elif category == "cross site scripting":
        return [
            "Sanitize user input",
            "Enable CSP headers",
            "Escape HTML output"
        ]

    elif category == "ransomware":
        return [
            "Isolate infected host",
            "Restore from backup",
            "Scan entire network"
        ]

    elif category == "malware":
        return [
            "Run antivirus scan",
            "Quarantine infected system",
            "Update antivirus signatures"
        ]

    elif category == "brute force":
        return [
            "Block attacker IP",
            "Enable MFA",
            "Reset compromised password"
        ]

    return [
        "Investigate manually"
    ]