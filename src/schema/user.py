from pydantic import BaseModel, Field, EmailStr

class BaseUser(BaseModel):
    name: str = Field(...,min_length=3,max_length=20)
    email: EmailStr
    password: str = Field(...,min_length=8,max_length=12)

class ResponseUser(BaseModel):
    name: str 
    email: str 