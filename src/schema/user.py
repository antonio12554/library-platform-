from pydantic import BaseModel, Field, EmailStr
from src.schema.book import Book
from src.schema.favorite import ResponseFavorityBook

class BaseUser(BaseModel):
    name: str = Field(...,min_length=3,max_length=20)
    email: EmailStr
    password: str = Field(...,min_length=8,max_length=12)

class ResponseUser(BaseModel):
    id: int
    name: str 
    email: str 
    favorite: list["ResponseFavorityBook"]
