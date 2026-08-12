from fastapi import Header,Depends
from src.auth.jwt_hantler import validate_token,get_user

def get_current_token(authorization: str = Header()):
    access_token: str = authorization.split(" ")[1]
    validate: object = validate_token(access_token)
    user_id: int = get_user(validate)
    return user_id
    
