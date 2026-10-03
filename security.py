import jwt
from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
def create_access_token(user_id: int):
    payload = {
        "sub" : str(user_id),
   
    }
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token