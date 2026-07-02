from app.config.settings import settings


def generate_summary(title: str, description: str):

    if settings.OPENAI_API_KEY == "":

        return description[:100]

    # Future:
    # GPT summary yahan generate hogi

    return description[:100]