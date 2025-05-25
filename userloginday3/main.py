from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext

# from . import models, schemas, database
import models
import schemas
import database

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


@app.post("/signup", response_model=schemas.UserOut)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    # Check if username already exists
    if db.query(models.User).filter(models.User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        email=user.email, username=user.username, hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users", response_model=list[schemas.UserOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
