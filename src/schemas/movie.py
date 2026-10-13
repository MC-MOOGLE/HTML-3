from pydantic import BaseModel, ConfigDict, Field


class MovieCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    year: int = Field(ge=1888, le=2100)
    rating: float = Field(default=0.0, ge=0, le=10)


class MovieUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    year: int | None = Field(default=None, ge=1888, le=2100)
    rating: float | None = Field(default=None, ge=0, le=10)


class MovieRead(MovieCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
