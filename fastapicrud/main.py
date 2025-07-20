from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models
import schema.schemas as schemas
import crudOperations.crud as crud
import crudOperations.bookcrud as bookcrud
import auth
import schema.bookSchema
import schema.schemas
from fastapi import Path
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    return crud.create_user(db, user)


@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}


# # book
# @app.post("/books", response_model=schema.bookSchema.BookOut)
# def create_book(
#     book: schema.bookSchema.BookCreate,
#     db: Session = Depends(get_db),
#     user: schema.schemas.UserLogin = Depends(),
# ):
#     return bookcrud.create_book(db, book, user_id=1)


# @app.get("/books/", response_model=List[schema.bookSchema.BookOut])
# def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     return bookcrud.get_book


# @app.get("/books/{book_id}", response_model=schema.bookSchema.BookOut)
# def read_book(book_id: int = Path(...), db: Session = Depends(get_db)):
#     book = bookcrud.get_book(db, book_id)
#     if not book:
#         raise HTTPException(status_code=404, detail="book Not Found")
#     return book
