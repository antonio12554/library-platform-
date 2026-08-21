from pydantic import BaseModel, Field
from src.schema.category import ResponseCategory
from src.schema.genre import BaseGenre

class Book(BaseModel):
    id: int
    title: str 
    subtitle: str 
    author: str 
    description: str = Field(...,max_length=400)
    pdf_url: str
    number_page: int
    created_at: str
    book_cover_image_url: str

class ResponseBook(Book):
    category: ResponseCategory
    genre: list["BaseGenre"]