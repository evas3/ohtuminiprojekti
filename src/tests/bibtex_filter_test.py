import unittest
from services.bibtex_filter import BibtexFilter

test_case1 = [
'@book{123,',
'  author    = Testi,',
'  title     = test,',
'  publisher = Test,',
'  year      = 2023,',
'  address   = Test ',
'}' ]

class TestBibtex_filter(unittest.TestCase):
    def setUp(self):
        self.filter = BibtexFilter()
        self.test_case1 = []
        self.test_case1.append(test_case1)

    def test_filter_finds_match(self):
        result = self.filter.filter_by("author", "Testi", self.test_case1)
        self.assertNotEqual(result, [])

    def test_filter_does_not_find_match(self):
        result = self.filter.filter_by("author", "Testaaja", self.test_case1)
        self.assertEqual(result, [])