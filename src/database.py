import os

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./movies.db")

engine = create_async_engine(DATABASE_URL, poolclass=NullPool)
session_factory = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_session():
    async with session_factory() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
