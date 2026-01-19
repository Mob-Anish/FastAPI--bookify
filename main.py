from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class BookCreateModel(BaseModel):
    title: str
    author: str


@app.get('/')
async def read_root():
    return {"message": "Hello world"}


@app.get('/greet')
async def greet_name(name: Optional[str] = 'User', age: int = 0) -> dict:
    return {"message": f"Hello {name}", "age": age}


@app.post('/create_book')
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }


@app.get('/get_headers')
async def get_headers(accept: str = Header(None), content_type: str = Header(None), user_agent: str = Header(None)):
    request_headers = {}
    request_headers['Accept'] = accept
    request_headers['Content-Type'] = content_type
    request_headers['User-Agent'] = content_type

    return request_headers
