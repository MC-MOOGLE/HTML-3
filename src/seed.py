import asyncio

from src.database import Base, engine, session_factory
from src.models.movie import Movie

SEED_MOVIES = [
    {"title": "Матрица", "year": 1999, "rating": 8.5},
    {"title": "Интерстеллар", "year": 2014, "rating": 8.6},
    {"title": "Начало", "year": 2010, "rating": 8.7},
    {"title": "Аватар", "year": 2009, "rating": 7.9},
    {"title": "Титаник", "year": 1997, "rating": 7.8},
    {"title": "Дюна", "year": 2021, "rating": 8.0},
    {"title": "Довод", "year": 2020, "rating": 7.3},
]

async def _reset_and_seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    async with session_factory() as session:
        session.add_all([Movie(**data) for data in SEED_MOVIES])
        await session.commit()

def reset_and_seed():
    asyncio.run(_reset_and_seed())

if __name__ == "__main__":
    reset_and_seed()
