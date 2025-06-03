from src.library_repository import LibraryRepository


class InMemoryRepository(LibraryRepository):

    def __init__(self):
        self.books = {}

    def add_book(self, title: str, author: str, year: int):
        self.books[title] = {"author": author, "year": year}

    def remove_book(self, title: str) -> bool:
        return self.books.pop(title, None) is not None

    def get_all_books(self) -> list:
        return [{"title": title, "author": data["author"], "year": data["year"]} for title, data in self.books.items()]