"""
History API

Returns previous investigations.
"""

from fastapi import APIRouter

from app.services.investigation_store import get_history

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("")
def history():

    return get_history()