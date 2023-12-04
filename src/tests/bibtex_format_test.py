import unittest
from bibtex_format import Bibtex

class TestBibtex_format(unittest.TestCase):
    def setUp(self):
        self.bibtex_format = Bibtex()

    def test_key(self):
        test_short = self.bibtex_format.key("", 0)
        right_short = "0"
        test_longer = self.bibtex_format.key("honda", 20000)
        right_longer = "hon20000"
        
        self.assertEqual(test_short, right_short)
        self.assertEqual(test_longer, right_longer)

    def test_book(self):
        test = self.bibtex_format.book("title", "author", 2023, "publisher", "address")
        right = """
@Book{aut2023,
  author    = {author},
  title     = {title},
  publisher = {publisher},
  year      = {2023},
  address   = {address}
}"""
        self.assertEqual(test, right)

    def test_article(self):
        test = self.bibtex_format.article("author", "title", "journal", 2023, "volume", "1--2")
        right = """
@article{aut2023,
  author  = {author},
  title   = {title},
  journal = {journal},
  year    = {2023},
  volume  = {volume},
  pages   = {1--2}
}"""

        self.assertEqual(test, right)
    
    def test_inproceedings(self):
        test = self.bibtex_format.inproceedings("author", "title", "booktitle", 2023)
        right = """
@inproceedings{aut2023,
  author    = {author},
  title     = {title},
  booktitle = {booktitle},
  year      = {2023},
}"""

        self.assertEqual(test, right)