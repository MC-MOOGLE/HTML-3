from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    year: Mapped[int] = mapped_column(Integer)
    rating: Mapped[float] = mapped_column(Float, default=0.0)
