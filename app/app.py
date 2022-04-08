from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.users.repository import create_db_and_tables
from app.users.models import UserDB
from app.users import current_active_user
from app.users.controller import (
    auth_jwt_router,
    get_register_router,
    get_reset_password_router,
    get_verify_router,
    get_users_router,
)

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_jwt_router)
app.include_router(get_register_router)
app.include_router(get_reset_password_router)
app.include_router(get_verify_router)
app.include_router(get_users_router)


@app.get("/authenticated-route")
async def authenticated_route(user: UserDB = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
