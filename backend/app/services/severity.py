def calculate_severity(description: str):

    text = description.lower()

    if "critical" in text:
        return "CRITICAL"

    elif "high" in text:
        return "HIGH"

    elif "medium" in text:
        return "MEDIUM"

    return "LOW"