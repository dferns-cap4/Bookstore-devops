from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from time import sleep
import os
#Force tests
app = FastAPI()

# ---- Mock Data Storage ----
fake_books_db = []

# ---- Schemas ----
class BookCreate(BaseModel):
    title: str
    author: str

class BookResponse(BookCreate):
    id: int

class HealthCheckResponse(BaseModel):
    message: str

# ---- Endpoints ----

@app.post("/books/", response_model=BookResponse)
async def create_book(book: BookCreate):
    new_book = BookResponse(id=len(fake_books_db) + 1, **book.dict())
    fake_books_db.append(new_book)
    return new_book

@app.get("/books/", response_model=List[BookResponse])
async def get_books():
    return fake_books_db

@app.get("/health-check/", response_model=HealthCheckResponse)
async def healthCheck():
    return HealthCheckResponse(message="sick")
#Added information

@app.get("/load")
async def simulate_load():
    container_id = os.getenv("HOSTNAME")
    sleep(15)
    return {"handled_by": container_id}