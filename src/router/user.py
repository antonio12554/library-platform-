#database
from src.core.db import get_db
from sqlalchemy.orm import Session
#models
from src.model.model import User
#schemas
from src.schema.user import BaseUser,ResponseUser
#fastapi
from fastapi import APIRouter,Depends
#crud
from src.crud.crud import create,read,read_by_id
#auth
from src.auth.segurity import create_hash_password

router = APIRouter(tags=["User"])

@router.post("/login")
def login(validate: BaseUser, db: Session = Depends(get_db)):
    hash_password: str = create_hash_password(validate.password)
    data: object = User(name=validate.name, email=validate.email, hash_password=hash_password)
    return create(db,data)

@router.get("/prefile/{id}",response_model=ResponseUser)
def prefile(id, db: Session = Depends(get_db)):
    return read_by_id(db, User, id)

