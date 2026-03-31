from pydantic import BaseModel
class BlogCreate(BaseModel):
    title: str
    content: str
    is_published: bool = True
class BlogOut(BaseModel):
    id: int
    title: str
    content: str
    is_published: bool
    owner_id: int

    class Config:
        from_attribute = True