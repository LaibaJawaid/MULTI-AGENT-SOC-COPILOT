"""
Centralized LLM Service

All agents will use this file
instead of calling OpenAI directly.
"""

from openai import OpenAI

from app.config.settings import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


def ask_llm(prompt: str):

    response = client.chat.completions.create(

        model=settings.OPENAI_MODEL,

        messages=[

            {
                "role": "system",
                "content": (
                    "You are an expert SOC Level-3 Security Analyst."
                )
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        temperature=0.2

    )

    return response.choices[0].message.content