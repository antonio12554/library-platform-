import bcrypt

def create_hash_password(password: str):
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hash_password.decode("utf-8")

def validate_hash_password(password: str,hash_password: str):
    validate = bcrypt.checkpw(password.encode("utf-8") ,hash_password.encode("utf-8"))
    return validate

