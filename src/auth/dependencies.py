from fastapi import Header,Depends
from src.auth.jwt_hantler import validate_token,get_user

def get_current_token(authorization = Depends(Header)):
    access_token = authorization.split(" ")[1]
    validate = validate_token(access_token)
    user_id = get_user(validate)
    return user_id
    
