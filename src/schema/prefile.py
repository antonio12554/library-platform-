from pydantic import BaseModel
#schemas
from src.schema.favorite import ResponseFavorityBook
from src.schema.user import ResponseUser

class ResponsePrefile(BaseModel):
    user: ResponseUser
    favorite: list["ResponseFavorityBook"]

    

