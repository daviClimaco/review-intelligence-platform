from datetime import datetime

from pydantic import BaseModel, Field


class AuthorCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=150, examples=["João Silva"])


class AuthorUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=150, examples=["João Silva"])


class AuthorResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

    model_config = {"from_attributes": True}
