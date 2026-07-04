from openai import OpenAI

from app.config.settings import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def create_embedding(text):

    response = client.embeddings.create(

        model="text-embedding-3-small",

        input=text

    )

    return response.data[0].embedding