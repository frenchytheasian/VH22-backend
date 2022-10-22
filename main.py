from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from reddit import get_all_comments_from_post, get_top_n_posts, get_id_from_url

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    data = (get_all_comments_from_post(get_top_n_posts('news', 1)[0]))
    return {"message": data}

@app.post("/search/")
async def search(url: Union[str, None] = None):
    return {"message": "url"}