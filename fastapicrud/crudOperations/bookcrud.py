# import schema.bookSchema
# import models
# from sqlalchemy.orm import Session


# def create_book(db: Session, book: schema.bookSchema.BookCreate, user_id: int):
#     db_book = models.Book(**book.dict(), owner_id=user_id)
#     db.add(db_book)
#     db.commit()
#     db.refresh(db_book)
#     return db_book


# def get_books(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.Book).offset(skip).limit(limit).all()


# def get_book(db: Session, book_id: int):
#     return db.query(models.Book).filter(models.Book.id == book_id).first()


# def update_book(db: Session, book_id: int, book_data: schema.bookSchema.BookCreate):
#     book = db.query(models.Book).filter(models.Book.id == book_id).first()
#     if not book:
#         return None
#     for key, value in book_data.dict().items():
#         setattr(book, key, value)
#     db.commit()
#     db.refresh(book)
#     return book


# def delete_book(db: Session, book_id: int):
#     book = db.query(models.Book).filter(models.Book.id == book_id).first()
#     if book:
#         db.delete(book)
#         db.commit()
#     return book
