from app.db.qdrant import client

from app.db.qdrant import COLLECTION_NAME

from app.services.embedding import create_embedding


def search_similar(text: str):

    vector = create_embedding(text)

    results = client.search(

        collection_name=COLLECTION_NAME,

        query_vector=vector,

        limit=5

    )

    return results