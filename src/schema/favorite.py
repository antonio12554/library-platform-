from pydantic import BaseModel
from src.schema.book import ResponseBook

class ResponseFavorityBook(BaseModel):
    favotite_book: list["ResponseBook"]