from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sys, os

from reddit import get_all_comments_from_post, get_top_n_posts, get_id_from_url
from analytics import run_analytics

def enablePrint():
    sys.stdout = sys.__stdout__

class Search(BaseModel):
    url: str

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
async def search(item: Search):
    print(item)
    post_id = get_id_from_url(item.url)
    data = get_all_comments_from_post(post_id)
    sentiment_data = run_analytics(data)
    sentiment_data['comments'] = data
    
    enablePrint()
    
    return sentiment_data