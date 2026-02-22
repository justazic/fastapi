from fastapi import FastAPI

app = FastAPI()

books = []
authors = []
borrowed_books = []


@app.get("/books")
async def get_books():
    return books


@app.post("/books")
async def add_book(book: dict):
    books.append(book)
    return {"message": "Kitob qoshildi", "data": book}


@app.get("/authors")
async def get_authors():
    return authors


@app.post("/authors")
async def add_author(author: dict):
    authors.append(author)
    return {"message": "Muallif qoshildi", "data": author}


@app.get("/borrowed_books")
async def get_borrowed_books():
    return borrowed_books


@app.post("/borrowed_books")
async def borrow_book(data: dict):
    borrowed_books.append(data)
    return {"message": "Kitob ijaraga olindi", "data": data}