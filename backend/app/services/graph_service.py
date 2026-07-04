from app.db.neo4j import get_session


def create_alert_graph(alert):

    query = """

    MERGE (a:Alert {id:$id})

    SET

        a.title=$title,

        a.severity=$severity

    """

    with get_session() as session:

        session.run(

            query,

            id=alert.id,

            title=alert.title,

            severity=alert.severity

        )

    return True

def connect_alert_user(alert_id,user):

    query="""

    MATCH (a:Alert{id:$aid})

    MERGE (u:User{name:$user})

    MERGE (u)-[:TRIGGERED]->(a)

    """

    with get_session() as session:

        session.run(

            query,

            aid=alert_id,

            user=user

        )

def connect_device(alert_id,device):

    query="""

    MATCH (a:Alert{id:$aid})

    MERGE(d:Device{name:$device})

    MERGE(d)-[:GENERATED]->(a)

    """

    with get_session() as session:

        session.run(

            query,

            aid=alert_id,

            device=device

        )

def get_related(alert_id):

    query="""

    MATCH (n)-[r]->(a:Alert{id:$id})

    RETURN

    n,

    r,

    a

    """

    with get_session() as session:

        result=session.run(

            query,

            id=alert_id

        )

        return [record.data() for record in result]