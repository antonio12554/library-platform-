from pydantic import BaseModel

class ResponseCategory(BaseModel):
    category: str

    