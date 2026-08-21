import jwt
from datetime import datetime,timezone,timedelta
from fastapi import HTTPException
#secret key
from src.config import settings

def generate_access_token(id_user: int):
    expiration_date = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload: object = {"exp":int(expiration_date.timestamp()),"sub":str(id_user)}
    access_token: str = jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)
    return access_token

def validate_token(token: str):
    try:
        payload = jwt.decode(token, settings.secret_key,algorithms=[settings.algorithm])
        return payload
    except jwt.InvalidTokenError as error:
        raise(error)

def get_user(payload: object):
    user_id = int(payload["sub"])
    return user_id


    
