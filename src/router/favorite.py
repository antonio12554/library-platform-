#database
from src.core.db import get_db
from sqlalchemy.orm import Session
#models
from src.model.model import Favorite
#schemas
from src.schema.favorite import BaseFavorite
#fastapi
from fastapi import APIRouter,Depends
#crud
from src.crud.crud import create

router = APIRouter(tags=["favorite"])

@router.post("/favorite")
def favorite(validate: BaseFavorite, db: Session = Depends(get_db)):
    data: object = Favorite(user_id=validate.user_id, book_id=validate.book_id)
    return create(db, data)