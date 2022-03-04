# Created by vidit.singh at 04-03-2022

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Special methods or builtin/predefined methods for a class.

    def __str__(self):
        return f'Title fo the book is {self.title} written by {self.author} has {self.pages} pages'

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book has been deleted!")


book = Book('Magical Book', 'Vidit Singh', 500)
print(book)

print(book.__len__())
