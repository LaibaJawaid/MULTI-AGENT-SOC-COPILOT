from fastapi import APIRouter
from app.db.postgres import check_postgres
from app.db.redis import check_redis
from app.db.neo4j import check_neo4j
router = APIRouter(tags=["Health"])


@router.get("/health")
def health():
    return {
        "api": "running",
        "postgres": check_postgres(),
        "redis": check_redis(),
        "neo4j": check_neo4j()
    }

