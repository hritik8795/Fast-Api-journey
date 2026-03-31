from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # ✅ Add this line to complete the relationship
    books = relationship("Book", back_populates="owner")


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    description = Column(String)
    published_year = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # ✅ This must match User.books
    owner = relationship("User", back_populates="books")
