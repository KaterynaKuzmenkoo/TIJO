import unittest
from unittest.mock import Mock

from src.library import Library
from src.library_repository import LibraryRepository

from src.in_memory_repository import InMemoryRepository

class LibraryTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_repository = Mock(spec=LibraryRepository)
        self.library = Library(self.mock_repository)
        self.inMemoryRepository = InMemoryRepository()



    def test_add_one_book(self):
        title = "test"
        author = "TEST"
        year = 2000

        library = Library(InMemoryRepository())
        library.return_book(title, author, year)
        result = library.list_books()


        self.assertEqual(result, [{'author': author, 'title': title, 'year': year}])

    def test_remove_one_book(self):
        title = "test"
        author = "TEST"
        year = 2000


        library = Library(InMemoryRepository())
        library.return_book(title, author, year)
        library.borrow_book(title)
        result = library.list_books()


        self.assertEqual(result, [])


    def test_return_book_calls_add_book(self):
        title = "test"
        author = "TEST"
        year = 2000


        self.library.return_book(title, author, year)


        self.mock_repository.add_book.assert_called_once_with(title, author, year)

    def test_list_books_calls_get_all_books(self):
        title = "test"
        author = "TEST"
        year = 2000


        self.mock_repository.get_all_books.return_value = [{"title": title, "author": author, "year": year}]
        books = self.library.list_books()


        self.assertEqual(len(books), 1)
        self.assertEqual(books[0]["title"], title)
        self.mock_repository.get_all_books.assert_called_once()

    def test_borrow_book_calls_remove_book(self):
        return_value = True


        self.mock_repository.remove_book.return_value = return_value
        result = self.library.borrow_book("test")


        self.assertTrue(result)
        self.mock_repository.remove_book.assert_called_once_with("test")


if __name__ == '__main__':
    unittest.main()