from fastapi import APIRouter
from app.users import auth_backend, fastapi_users

auth_jwt_router = APIRouter(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    prefix="/auth/jwt",
    tags=["auth"],
)

get_register_router = APIRouter(
    fastapi_users.get_register_router(), prefix="/auth", tags=["auth"]
)

get_reset_password_router = APIRouter(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

get_verify_router = APIRouter(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)

get_users_router = APIRouter(
    fastapi_users.get_users_router(), prefix="/users", tags=["users"]
)
