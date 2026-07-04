from openai import OpenAI

from app.config.settings import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)


def ask_llm(prompt: str):

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {

                "role": "system",

                "content": "You are an expert SOC Analyst."

            },

            {

                "role": "user",

                "content": prompt

            }

        ],

        temperature=0.2

    )

    return response.choices[0].message.content