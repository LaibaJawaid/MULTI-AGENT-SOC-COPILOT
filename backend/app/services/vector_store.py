from qdrant_client.models import PointStruct

from app.db.qdrant import client

from app.db.qdrant import COLLECTION_NAME

from app.services.embedding import create_embedding


def store_alert(alert):

    vector = create_embedding(

        alert.title +

        " " +

        alert.description

    )

    point = PointStruct(

        id=alert.id,

        vector=vector,

        payload={

            "title": alert.title,

            "severity": alert.severity,

            "category": alert.category

        }

    )

    client.upsert(

        collection_name=COLLECTION_NAME,

        points=[point]

    )