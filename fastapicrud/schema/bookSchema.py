from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    published_year: Optional[int] = None


class BookCreate(BookBase):
    pass


class BookOut(BaseModel):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
