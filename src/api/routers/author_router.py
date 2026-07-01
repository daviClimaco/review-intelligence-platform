from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.api.routers.dependencies import get_db
from src.schemas.author_schema import AuthorCreate, AuthorResponse, AuthorUpdate
from src.services.author_service import AuthorService

router = APIRouter(
    prefix="/authors",
    tags=["Authors"],
)


@router.get("/", response_model=list[AuthorResponse])
def get_all_authors(db: Session = Depends(get_db)):
    return AuthorService(db).get_all()


@router.get("/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int, db: Session = Depends(get_db)):
    return AuthorService(db).get_by_id(author_id)


@router.post("/", response_model=AuthorResponse, status_code=status.HTTP_201_CREATED)
def create_author(data: AuthorCreate, db: Session = Depends(get_db)):
    return AuthorService(db).create(data)


@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(author_id: int, data: AuthorUpdate, db: Session = Depends(get_db)):
    return AuthorService(db).update(author_id, data)


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    AuthorService(db).delete(author_id)
