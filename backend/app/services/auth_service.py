"""
Authentication Service
"""

from app.auth.jwt_handler import create_token


def login(username: str, password: str):

    # TODO:
    # Verify database user

    if username == "admin" and password == "admin":

        return {

            "access_token": create_token(username),

            "token_type": "Bearer"

        }

    return {

        "error": "Invalid Credentials"

    }