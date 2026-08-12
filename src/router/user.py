#database
from src.core.db import get_db
from sqlalchemy.orm import Session
#models
from src.model.model import User
#schemas
from src.schema.user import BaseUser,ResponseUser
from src.schema.auth import BaseLogin
#fastapi
from fastapi import APIRouter,Depends, Header
#crud
from src.crud.crud import create,read_by_id,read_by_email
#auth
from src.auth.segurity import create_hash_password,validate_hash_password
from src.auth.dependencies import get_current_token
from src.auth.jwt_hantler import generate_access_token

router = APIRouter(tags=["User"])

@router.post("/create_account")
def create_account(validate: BaseUser, db: Session = Depends(get_db)):
    hash_password: str = create_hash_password(validate.password)
    data: object = User(name=validate.name, email=validate.email, hash_password=hash_password)
    return create(db, data)

@router.post("/login")
def login(validate: BaseLogin, db: Session = Depends(get_db)):
    user = read_by_email(db, User, validate.email)
    validate = validate_hash_password(validate.password, user.hash_password)
    if validate:
        access_token = generate_access_token(user.id)
        return {"token":access_token}

@router.get("/profile")
def prefile(user = Depends(get_current_token)):
    return user




