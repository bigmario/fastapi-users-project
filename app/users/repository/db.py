from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.users.models import UserDB
from app.config import Settings

from app.users.models.schemas import UserTable, Base


g_sets = Settings()

params = [
    g_sets.postgres_user,
    g_sets.postgres_password,
    g_sets.postgres_server,
    g_sets.postgres_port,
    g_sets.postgres_db,
]

DATABASE_URL = (
    f"postgresql+asyncpg://{params[0]}:{params[1]}@{params[2]}:{params[3]}/{params[4]}"
)
# DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(UserDB, session, UserTable)
