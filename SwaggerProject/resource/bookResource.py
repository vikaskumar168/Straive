# from flask_restful import Resource
# from flask import request
# import json
#
# books = [{"id": 1, "title": "Java book"},
#          {"id": 2, "title": "Python book"}]
#
#
# class BooksGETResource(Resource):
#     def get(self):
#         return books
#
# class BookGETResource(Resource):
#     def get(self, id):
#         for book in books:
#             if book["id"] == id:
#                 return book
#         return None
#
# class BookPOSTResource(Resource):
#     def post(self):
#         book = json.loads(request.data)
#         new_id = max(book["id"] for book in books) + 1
#         book["id"] = new_id
#         books.append(book)
#         return book
#
#
# class BookPUTResource(Resource):
#     def put(self, id):
#         book = json.loads(request.data)
#         for _book in books:
#             if _book["id"] == id:
#                 _book.update(book)
#                 return _book
#
#
# class BookDELETEResource(Resource):
#     def delete(self, id):
#         global books
#         books = [book for book in books if book["id"] != id]
#         return "", 204


from flask_restful import Resource
from flask import request
from models.bookModels import Book, db

class BooksGETResource(Resource):
    def get(self):
        books = Book.query.all()
        return [book.to_dict() for book in books]

class BookGETResource(Resource):
    def get(self, id):
        book = Book.query.get(id)
        return book.to_dict() if book else {"error": "Book not found"}, 404

class BookPOSTResource(Resource):
    def post(self):
        data = request.get_json()
        book = Book(title=data['title'])
        db.session.add(book)
        db.session.commit()
        return book.to_dict(), 201

class BookPUTResource(Resource):
    def put(self, id):
        data = request.get_json()
        book = Book.query.get(id)
        if not book:
            return {"error": "Book not found"}, 404
        book.title = data['title']
        db.session.commit()
        return book.to_dict()

class BookDELETEResource(Resource):
    def delete(self, id):
        book = Book.query.get(id)
        if not book:
            return {"error": "Book not found"}, 404
        db.session.delete(book)
        db.session.commit()
        return "", 204
