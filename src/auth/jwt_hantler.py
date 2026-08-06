import jwt
from datetime import datetime,timezone,timedelta
#secret key
from src.config import settings

def generate_access_token(id_user: int):
    time = (datetime.now(timezone.utc) + timedelta(minutes=30)).time()
    payload: object = {"exp":time,"sub":id_user}
    access_token: str = jwt.encode(payload=payload, secret_key=settings.secret_key,algorithm=settings.algorithm)
    return access_token

def validate_token(token: str):
    try:
        payload = jwt.decode(token, settings.secret_key,algorithms=[settings.algorithm])
        return payload
    except jwt.InvalidTokenError:
        return None

def get_user(payload: object):
    user_id = payload.get("sub")
    return user_id

    
