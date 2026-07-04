from app.services.rag_service import (

    retrieve_similar,

    store_alert

)


class RagAgent:

    def store(self, alert):

        store_alert(alert)

    def retrieve(self, alert):

        return retrieve_similar(alert)


rag_agent = RagAgent()