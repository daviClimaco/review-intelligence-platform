from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.database.base import Base

class Category(Base):

    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100),nullable=False,unique=True)

    created_at: Mapped[DateTime] = mapped_column(DateTime,server_default=func.now())
