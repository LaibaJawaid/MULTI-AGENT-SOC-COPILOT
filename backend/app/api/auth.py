"""
Authentication API
"""

from fastapi import APIRouter

from app.schemas.auth import LoginRequest

from app.services.auth_service import login

router = APIRouter(

    prefix="/auth",

    tags=["Authentication"]

)


@router.post("/login")

def authenticate(user: LoginRequest):

    return login(

        user.username,

        user.password

    )