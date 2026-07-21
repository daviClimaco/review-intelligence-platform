from sqlalchemy.orm import Session

from src.models.author import Author
from src.schemas.author_schema import AuthorCreate, AuthorUpdate


class AuthorRepository:

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Author]:
        return self.db.query(Author).order_by(Author.id).all()

    def get_by_id(self, author_id: int) -> Author | None:
        return self.db.query(Author).filter(Author.id == author_id).first()

    #21/07/2026 - davi
    def get_by_name(self, name: str) -> Author | None:
        return self.db.query(Author).filter(Author.name == name).first()

    def create(self, data: AuthorCreate) -> Author:
        author = Author(**data.model_dump())
        self.db.add(author)
        self.db.commit()
        self.db.refresh(author)
        return author

    def update(self, author: Author, data: AuthorUpdate) -> Author:
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(author, field, value)
        self.db.commit()
        self.db.refresh(author)
        return author

    def delete(self, author: Author) -> None:
        self.db.delete(author)
        self.db.commit()
