from neo4j import GraphDatabase

from app.config.settings import settings


driver = GraphDatabase.driver(

    settings.NEO4J_URI,

    auth=(

        settings.NEO4J_USERNAME,

        settings.NEO4J_PASSWORD

    )

)


def get_session():

    return driver.session()


def check_neo4j():

    try:

        with driver.session() as session:

            session.run("RETURN 1")

        return True

    except Exception as e:

        print(e)

        return False
    
def search_vectors(query: str):
    return []

def search_iocs(query: str):
    return []