from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.auth.jwt_hantler import validate_token,get_user

segurity = HTTPBearer()

def get_current_token(credentials: HTTPAuthorizationCredentials = Depends(segurity)):
    token = credentials.credentials
    validate: object = validate_token(token)
    user_id: int = get_user(validate)
    return user_id
    
