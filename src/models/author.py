from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from src.database.base import Base

if TYPE_CHECKING:
    from src.models.review import Review


class Author(Base):

    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(150), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )

    reviews: Mapped[list[Review]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
    )
