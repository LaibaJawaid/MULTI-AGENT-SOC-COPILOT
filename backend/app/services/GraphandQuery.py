from app.db.neo4j import driver


def get_related(category):

    query = """

    MATCH (a)-[:HAS_CATEGORY]->

    (c {name:$category})

    RETURN a.title

    """

    with driver.session() as session:

        result = session.run(

            query,

            category=category

        )

        return [

            record["a.title"]

            for record in result

        ]