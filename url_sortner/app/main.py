from fastapi import FastAPI
from app.api.routes import url
from app.core.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(url.router)   