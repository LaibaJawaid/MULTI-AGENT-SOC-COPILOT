from app.config.settings import settings


def get_database_status():
    return {
        "postgres": settings.POSTGRES_HOST,
        "redis": settings.REDIS_HOST,
        "qdrant": settings.QDRANT_URL,
        "neo4j": settings.NEO4J_URI,
    }