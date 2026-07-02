def summarize_alert(title: str, description: str):

    if len(description) <= 80:
        return description

    return description[:80] + "..."