#database
from sqlalchemy.orm import Session
from src.core.db import get_db
#models
from src.model.model import Book
#schema
from src.schema.book import ResponseBook
#fastapi
from fastapi import APIRouter,Depends
#crud
from src.crud.crud import read,read_by_id

#routes
router = APIRouter(tags=["Book"])

@router.get("/book",response_model=list[ResponseBook])
def book(db: Session = Depends(get_db)):
    return read(db, Book)

@router.get("/book/{id}",response_model=ResponseBook)
def book(id,db: Session = Depends(get_db)):
    return read_by_id(db, Book, id)


