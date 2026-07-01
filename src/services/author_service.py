from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.models.author import Author
from src.repositories.author_repository import AuthorRepository
from src.schemas.author_schema import AuthorCreate, AuthorResponse, AuthorUpdate


class AuthorService:

    def __init__(self, db: Session) -> None:
        self.repository = AuthorRepository(db)

    def get_all(self) -> list[AuthorResponse]:
        return self.repository.get_all()

    def get_by_id(self, author_id: int) -> Author:
        author = self.repository.get_by_id(author_id)
        if not author:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Author with id {author_id} not found.",
            )
        return author

    def create(self, data: AuthorCreate) -> AuthorResponse:
        return self.repository.create(data)

    def update(self, author_id: int, data: AuthorUpdate) -> AuthorResponse:
        author = self.get_by_id(author_id)
        return self.repository.update(author, data)

    def delete(self, author_id: int) -> None:
        author = self.get_by_id(author_id)
        self.repository.delete(author)
