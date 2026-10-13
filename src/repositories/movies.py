from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.movie import Movie
from src.schemas.movie import MovieCreate

async def create_movie(session: AsyncSession, data: MovieCreate) -> Movie:
    new_movie = Movie(**data.model_dump())
    session.add(new_movie)
    await session.commit()
    await session.refresh(new_movie)
    return new_movie

async def get_movie(session: AsyncSession, movie_id: int) -> Movie | None:
    return await session.get(Movie, movie_id)

async def get_list_movies(
    session: AsyncSession,
    limit: int = 50,
    offset: int = 0
    ) -> list[Movie]:
    limit = max(1, min(limit, 100))
    offset = max(0, offset)
    query = select(Movie).order_by(Movie.id.asc()).offset(offset).limit(limit)
    result = await session.execute(query)
    return list(result.scalars().all())
