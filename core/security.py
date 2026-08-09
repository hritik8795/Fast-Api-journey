# from passlib.context import CryptContext
# from jose import jwt

# SECRET_KEY = "BLOGAPPSECRETKEY"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")   

# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# def verify_password(password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(password, hashed_password)

# def create_access_token(data:dict):
#     return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


from pwdlib import PasswordHash
from jose import jwt


SECRET_KEY = "BLOGAPPSECRETKEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)


def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)