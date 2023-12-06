# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()
#
# class Book(BaseModel):
#     title: str
#     author: str
#     publication_year: int
#
# @app.get("/books", response_model=list[Book])
# def get_books():
#     return [{"title": "Book 1", "author": "Author 1", "publication_year": 2001}, {"title": "Book 2", "author": "Author 2", "publication_year": 2002}]
#
# @app.post("/books", response_model=Book)
# def add_book(book: Book):
#     return book
