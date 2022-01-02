from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    Title: str
    Title2: str
    Published: bool = True

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"Data":"Test Post"}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.Published)
    return {"data" : "New Post Added."}