from app.rag.embeddings import create_embedding

from app.rag.qdrant_store import (

    insert_vector,

    search_similar

)


def store_alert(alert):

    text = f"""

Title:

{alert.title}

Description:

{alert.description}

Severity:

{alert.severity}

"""

    embedding = create_embedding(text)

    insert_vector(

        alert.id,

        embedding,

        {

            "title": alert.title,

            "severity": alert.severity

        }

    )


def retrieve_similar(alert):

    text = f"""

{alert.title}

{alert.description}

"""

    embedding = create_embedding(text)

    return search_similar(embedding)