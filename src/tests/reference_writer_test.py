import unittest

from repositories.reference_writer import ReferenceWriter

test_case_valid = """
    @Book{123,
      author    = {Testi},
      title     = {testi},
      publisher = {Testi},
      year      = {2023}
    }
    """

test_case_invalid_encoding = "Hello, World! \ud800"

class TestReferenceWriter(unittest.TestCase):
    def setUp(self):
        self.writer = ReferenceWriter()

    def test_file_is_written(self):
        self.assertEqual(self.writer.write(test_case_valid), True)

    def test_test_file_is_not_written_invalid_encoding(self):
        self.assertEqual(self.writer.write(test_case_invalid_encoding), False)
