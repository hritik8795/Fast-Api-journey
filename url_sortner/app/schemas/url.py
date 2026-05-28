from pydantic import BaseModel

class URLBase(BaseModel):
    original_url: str

class URLCreate(URLBase):
    original_url: str

class URLResponse(BaseModel):
    original_url:str
    short_url:str
    short_url:str

    class Config:
        orm_mode =True
