import unittest
from ui.ui import Ui
from bibtex_format import Bibtex

class BibtexStub:
    def book(self):
        return {
            "key": "{1}",
            "author": "{testi}",
            "title": "{testi}",
            "publisher": "{testi}",
            "year": "{testi}",
            "address": "{testi}"
        }

class TestUi(unittest.TestCase):
    def setUp(self):
        self.bibtex_stub = BibtexStub()
        self.ui = Ui(self.bibtex_stub)

    def test_book_citation_is_added_correctly(self):
        key = "TestKey"
        title = "TestTitle"
        author = "TestAuthor"
        year = "2023"
        publisher = "TestPublisher"
        address = "TestAddress"

        function_citation = self.ui.add_book_citation(key, title, author, year, publisher, address)
        stub_citation = self.bibtex_stub.book(key, title, author, year, publisher, address)

        self.assertEqual(function_citation, stub_citation)