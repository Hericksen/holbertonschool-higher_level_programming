#!/usr/bin/python3

class Library:

    max_books_number = 100

    def __init__(self, name):
        self._library_name = name
        self._number_of_books = 0
        self._books_by_author = {}

    @property
    def name(self):
        return self._library_name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._library_name = value
        print(f"Name of the library has been setted to {self._library_name}")

    @property
    def number_of_books(self):
        return self._number_of_books

    @property
    def authors(self):
        return self._books_by_author

    def add_author(self, author: str):
        if author in self.authors.keys():
            raise KeyError("The author already exists")
        if not isinstance(author, str):
            raise TypeError("The author must be a string")
        self._books_by_author[author] = []
        print(f"The author {author} has been added to the library")

    def add_book(self, author: str, title: str):
        if self._number_of_books < Library.max_books_number:
            if author not in self._books_by_author.keys():
                self.add_author(author)
            if title in self._books_by_author[author]:
                raise ValueError("This book is already in the library")
            self._books_by_author[author].append(title)
            self._number_of_books += 1
            print(f"The book {title} has been added to the library")
        else:
            print("La bibliothèque est complète. Supprimez en un")

    def delete_book(self, author: str, title: str):
        if author not in self._books_by_author.keys():
            raise KeyError("The author has not been found in the library")
        if title not in self._books_by_author[author]:
            raise ValueError(
                "The book has not been found in the library. Are you sure you gave the right title ?")
        self._books_by_author[author].remove(title)
        self._number_of_books -= 1
        print(f"The book {title} has been removed from the library")

    def get_books_by_author(self, author: str):
        if author not in self._books_by_author.keys():
            raise KeyError("The author has not been found in the library")
        return self._books_by_author[author]

    def get_book(self, author: str, title: str):
        if author not in self._books_by_author.keys():
            raise KeyError("The author has not been found in the library")
        if title not in self._books_by_author[author]:
            raise ValueError(
                "The book has not been found in the library. Are you sure you gave the right title ?")
        for book in self._books_by_author[author]:
            if book == title:
                return (book)


class ComicLibrary(Library):

    def __init__(self, name: str):
        super().__init__(name) = name
        self._series = {}

    def add_book(self, author: str, title: str,
                 serie: str, artist: str):
        if serie not in self._series:
            self._series[serie] = []
        if title in self._series[serie]:
            raise ValueError("Le titre existe déjà*")
        super().add_book(author, title)
        self._series[serie].append(title)
        self._series[serie].append(artist)

    def get_books_by_series(self, serie: str):
