def classify_alert(title: str, description: str):

    text = f"{title} {description}".lower()

    if "sql" in text:
        return "SQL Injection"

    elif "xss" in text:
        return "Cross Site Scripting"

    elif "ransomware" in text:
        return "Ransomware"

    elif "bruteforce" in text:
        return "Brute Force"

    elif "malware" in text:
        return "Malware"

    return "Unknown"