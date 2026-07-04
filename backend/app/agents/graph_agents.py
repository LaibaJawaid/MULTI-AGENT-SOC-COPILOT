from app.services.graph_service import (

    create_alert_graph,

    connect_alert_user,

    connect_device,

    get_related

)


class GraphAgent:

    def build(self,alert):

        create_alert_graph(alert)

        connect_alert_user(

            alert.id,

            "Unknown User"

        )

        connect_device(

            alert.id,

            "Unknown Device"

        )

    def investigate(self,id):

        return get_related(id)


graph_agent=GraphAgent()