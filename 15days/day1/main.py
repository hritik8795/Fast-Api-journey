# pip install -r requirements.txt
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World!"}


@app.get("/greet/{name}")
def greet_name(name: str):
    return {"greeting": f"hello,{name}!"}
