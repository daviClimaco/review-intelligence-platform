from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from database.base import Base
from models.author import Author
from models.category import Category


class Review(Base):

    __tablename__ = "review"

    id: Mapped[int] = mapped_column(primary_key=True)

    author_id: Mapped[int] = mapped_column(
        ForeignKey("author.id"),
        nullable=False
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.id"),
        nullable=False
    )

    rating: Mapped[float] = mapped_column(
        Numeric(2, 1),
        nullable=False
    )

    review_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    sentiment: Mapped[str] = mapped_column(
        String(20)
    )

    platform: Mapped[str] = mapped_column(
        String(50)
    )

    review_date: Mapped[datetime] = mapped_column(
        DateTime
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    author: Mapped[Author] = relationship()

    category: Mapped[Category] = relationship()
