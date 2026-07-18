from pydantic import BaseModel, Field
from src.schema.category import ResponseCategory


class ResponseBook(BaseModel):
    id: int
    title: str 
    subtitle: str 
    author: str 
    description: str = Field(...,min_length=50,max_length=200)
    pdf_url: str
    number_page: int
    created_at: str
    book_cover_image_url: str
    Category: ResponseCategory