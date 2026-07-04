from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

from app.config.settings import settings
from qdrant_client.models import PointStruct

client = QdrantClient(url=settings.QDRANT_URL)

COLLECTION = "alerts"


def create_collection():

    collections = client.get_collections().collections

    names = [c.name for c in collections]

    if COLLECTION not in names:

        client.create_collection(

            collection_name=COLLECTION,

            vectors_config=VectorParams(

                size=1536,

                distance=Distance.COSINE

            )

        )


def insert_vector(alert_id, embedding, payload):

    client.upsert(

        collection_name=COLLECTION,

        wait=True,

        points=[

            PointStruct(

                id=alert_id,

                vector=embedding,

                payload=payload

            )

        ]

    )


def search_similar(vector):

    return client.search(

        collection_name=COLLECTION,

        query_vector=vector,

        limit=5

    )