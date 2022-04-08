from fastapi import APIRouter
from app.users.service import auth_backend, fastapi_users

auth_jwt_router = fastapi_users.get_auth_router(
    auth_backend, requires_verification=True
)

get_register_router = fastapi_users.get_register_router()

get_reset_password_router = fastapi_users.get_reset_password_router()

get_verify_router = fastapi_users.get_verify_router()

get_users_router = fastapi_users.get_users_router()
