from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from src.database.base import Base
from src.models.author import Author
from src.models.category import Category


class Review(Base):

    __tablename__ = "review"

    id: Mapped[int] = mapped_column(primary_key=True)

    author_id: Mapped[int] = mapped_column(
        ForeignKey("author.id"),
        nullable=False,
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.id"),
        nullable=False,
    )

    rating: Mapped[float] = mapped_column(
        Numeric(2, 1),
        nullable=False,
    )

    review_text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # Preenchido futuramente pelo pipeline de ML/NLP
    sentiment: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    platform: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    review_date: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )

    author: Mapped[Author] = relationship(back_populates="reviews")

    category: Mapped[Category] = relationship(back_populates="reviews")
