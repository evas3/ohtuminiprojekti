import unittest

from repositories.reference_writer import ReferenceWriter

test_case_valid = """
@Book{123,
  author    = {Testi},
  title     = {testi},
  publisher = {Testi},
  year      = {2023},
  address   = {Testi}
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

    def test_read_file_method_works_on_new_file(self):
        self.writer.new_filename("testing")
        result = self.writer.read_file()
        self.assertEqual(result, [])

    def test_summarize_returns_error_when_file_not_found(self):
        self.writer.short_data_file_path += ".bib"
        result = self.writer.summarize()
        self.assertEqual(result, [])

    def test_write_shortform_works_with_invalid_entry(self):
        result = self.writer.write_shortform(test_case_invalid_encoding, "testi", 2023)
        self.assertEqual(result, False)

    def test_write_shortform_works_with_valid_entry(self):
        result = self.writer.write_shortform("Book", "testi", 2023)
        self.assertEqual(result, True)
