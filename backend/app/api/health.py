from fastapi import APIRouter
from app.db.database import get_database_status

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "services": get_database_status()
    }