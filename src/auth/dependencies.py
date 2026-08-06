from fastapi import Header,Depends
import jwt
from src.config import settings
from src.auth.jwt_hantler import validate_token,get_user

def get_current_token(authorization = Depends(Header)):
    access_token = authorization.split(" ")[1]
    validate_token = validate_token(access_token)
    user_id = get_user(validate_token)
    return user_id
    
