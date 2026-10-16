from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import init_db
from src.routers.movies import router as movies_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="Movies API", lifespan=lifespan)
app.include_router(movies_router)

@app.get("/")
async def root():
    return {"message": "Movies API"}
