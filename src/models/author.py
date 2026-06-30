from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.base import Base

class Author(Base):

    __tablename__ = "author"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(150),nullable=False)

    created_at: Mapped[DateTime] = mapped_column(DateTime,server_default=func.now())
