# we are here study about path parameter and query parameter and Request validation


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# path parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "message": f"fetched user with id"}


# pip install -r requirements.txt


# query  parameter
@app.get("/search")
def search_user(name: str = "guest"):
    return {"message": f"hello ,{name}"}


# request Validation
class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, lt=120)
    email: str


@app.post("/create_user/")
async def create_user(user: User):
    return {"message": "user created successfully", "user": user}
