import unittest
from bibtex_format import Bibtex

class TestBibtex_format(unittest.TestCase):
    def setUp(self):
        self.bibtex_format = Bibtex()

    def test_book(self):
        test = self.bibtex_format.book("key", "author", "title", "publisher", 2023, "address")
        right = """
@Book{key,
  author    = {author},
  title     = {title},
  publisher = {publisher},
  year      = {2023},
  address   = {address}
}"""
        self.assertEqual(test, right)