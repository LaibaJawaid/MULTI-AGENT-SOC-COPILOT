"""
Qdrant Database Helper

Responsible for:

1. Connect Qdrant
2. Create collection
3. Generate embeddings
4. Search vectors
"""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from openai import OpenAI

from app.config.settings import settings

# ===========================================================
# Collection Name
# ===========================================================

COLLECTION_NAME = "soc_playbooks"

# ===========================================================
# Qdrant Client
# ===========================================================

client = QdrantClient(
    url=settings.QDRANT_URL
)

# ===========================================================
# OpenAI Client
# ===========================================================

openai_client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

# ===========================================================
# Create Collection
# ===========================================================

def create_collection():
    """
    Create collection if it doesn't exist.
    """

    collections = client.get_collections().collections

    names = [c.name for c in collections]

    if COLLECTION_NAME not in names:

        client.create_collection(

            collection_name=COLLECTION_NAME,

            vectors_config=VectorParams(

                size=1536,
                distance=Distance.COSINE

            )

        )

        print("Qdrant collection created.")

# ===========================================================
# Embedding Generator
# ===========================================================

def create_embedding(text: str):

    response = openai_client.embeddings.create(

        model=settings.OPENAI_EMBEDDING_MODEL,

        input=text

    )

    return response.data[0].embedding

# ===========================================================
# Search
# ===========================================================

def search_vectors(query: str):

    embedding = create_embedding(query)

    results = client.search(

        collection_name=COLLECTION_NAME,

        query_vector=embedding,

        limit=5

    )

    return results