from fastapi import FastAPI
from api import auth,blog

from db.database import engine
from models.user import User  
from db.database import Base

app = FastAPI()



@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
app.include_router(auth.router)
app.include_router(blog.router) 