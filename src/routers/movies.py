from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from src.repositories import movies as repo
from src.schemas.movie import MovieCreate, MovieRead, MovieUpdate

router = APIRouter(prefix="/movies", tags=["movies"])

@router.get("/", response_model=list[MovieRead])
async def list_movies(
    year_min: int | None = None,
    year_max: int | None = None,
    min_rating: float | None = None,
    order_by: str | None = "-rating",
    limit: int = 50,
    offset: int = 0,
    session: AsyncSession = Depends(get_session)
    ):
    return await repo.get_list_movies(
        session,
        year_min=year_min,
        year_max=year_max,
        min_rating=min_rating,
        order_by=order_by,
        limit=limit,
        offset=offset
    )

@router.get("/{movie_id}", response_model=MovieRead)
async def get_movie(movie_id: int, session: AsyncSession = Depends(get_session)):
    movie = await repo.get_movie(session, movie_id)
    if not movie: raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.post("/", response_model=MovieRead, status_code=status.HTTP_201_CREATED)
async def create_movie(data: MovieCreate, session: AsyncSession = Depends(get_session)):
    return await repo.create_movie(session, data)

@router.put("/{movie_id}", response_model=MovieRead)
async def put_movie(movie_id: int, data: MovieCreate, session: AsyncSession = Depends(get_session)):
    movie = await repo.put_movie(session, movie_id, data)
    if not movie: raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.patch("/{movie_id}", response_model=MovieRead)
async def patch_movie(movie_id: int, data: MovieUpdate, session: AsyncSession = Depends(get_session)):
    movie = await repo.patch_movie(session, movie_id, data)
    if not movie: raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(movie_id: int, session: AsyncSession = Depends(get_session)):
    if not await repo.delete_movie(session, movie_id):
        raise HTTPException(status_code=404, detail="Movie not found")
