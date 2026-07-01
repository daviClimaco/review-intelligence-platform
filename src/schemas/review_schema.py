from datetime import datetime

from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    author_id: int = Field(..., gt=0)
    category_id: int = Field(..., gt=0)
    rating: float = Field(..., ge=0.0, le=5.0, examples=[4.5])
    review_text: str = Field(..., min_length=1, examples=["Ótimo atendimento!"])
    sentiment: str | None = Field(None, max_length=20)
    platform: str | None = Field(None, max_length=50, examples=["Google Maps"])
    review_date: datetime | None = None


class ReviewUpdate(BaseModel):
    rating: float | None = Field(None, ge=0.0, le=5.0)
    review_text: str | None = Field(None, min_length=1)
    sentiment: str | None = Field(None, max_length=20)
    platform: str | None = Field(None, max_length=50)
    review_date: datetime | None = None


class ReviewResponse(BaseModel):
    id: int
    author_id: int
    category_id: int
    rating: float
    review_text: str
    sentiment: str | None
    platform: str | None
    review_date: datetime | None
    created_at: datetime

    model_config = {"from_attributes": True}
