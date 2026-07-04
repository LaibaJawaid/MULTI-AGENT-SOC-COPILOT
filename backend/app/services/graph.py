from app.db.neo4j import driver


def save_alert_graph(alert):

    query = """

    MERGE (a:Alert {title:$title})

    MERGE (c:Category {name:$category})

    MERGE (s:Severity {level:$severity})

    MERGE (a)-[:HAS_CATEGORY]->(c)

    MERGE (a)-[:HAS_SEVERITY]->(s)

    """

    with driver.session() as session:

        session.run(

            query,

            title=alert.title,

            category=alert.category,

            severity=alert.severity

        )