from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ---- Mock Data Storage ----
fake_books_db = []

# ---- Schemas ----
class BookCreate(BaseModel):
    title: str
    author: str

class BookResponse(BookCreate):
    id: int

# ---- Endpoints ----

@app.post("/books/", response_model=BookResponse)
async def create_book(book: BookCreate):
    new_book = BookResponse(id=len(fake_books_db) + 1, **book.dict())
    fake_books_db.append(new_book)
    return new_book

@app.get("/books/", response_model=List[BookResponse])
async def get_books():
    return fake_books_db
