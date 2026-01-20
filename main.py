from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Art of Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-01",
        "page_count": 464,
        "language": "English"
    },
    {
        "id": 2,
        "title": "Learning Python the Hard Way",
        "author": "Zed A. Shaw",
        "publisher": "O'Reilly Media",
        "published_date": "2017-06-30",
        "page_count": 320,
        "language": "English"
    },
    {
        "id": 3,
        "title": "JavaScript: The Definitive Guide",
        "author": "David Flanagan",
        "publisher": "O'Reilly Media",
        "published_date": "2020-05-08",
        "page_count": 706,
        "language": "English"
    },
    {
        "id": 4,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "publisher": "MIT Press",
        "published_date": "2009-07-31",
        "page_count": 1312,
        "language": "English"
    },
    {
        "id": 5,
        "title": "You Don’t Know JS Yet",
        "author": "Kyle Simpson",
        "publisher": "Independently Published",
        "published_date": "2020-01-28",
        "page_count": 143,
        "language": "English"
    }
]


@app.get('/books')
async def get_all_books() -> list:
    pass


@app.get('/books')
async def create_book() -> dict:
    pass


@app.get('/book/{book_id}')
async def get_book(book_id: int) -> dict:
    pass


@app.get('/book/{book_id}')
async def update_book(book_id: int) -> dict:
    pass


@app.get('/book/{book_id}')
async def delete_book(book_id: int) -> dict:
    pass
