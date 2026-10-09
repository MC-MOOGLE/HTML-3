from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="Movies API", lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Movies API"}
