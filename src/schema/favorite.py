from pydantic import BaseModel
from src.schema.book import Book

class ResponseFavorityBook(BaseModel):
    book_id: int

class BaseFavorite(BaseModel):
    user_id: int
    book_id: int