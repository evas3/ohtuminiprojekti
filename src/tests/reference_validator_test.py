import unittest
from reference_validator import ValidateParameters

class TestReferenceValidator(unittest.TestCase):
    def setUp(self):
        self.reference_validator = ValidateParameters()

    def test_validate_parameters_book(self):
        test = self.reference_validator.validate_parameters_book("Test", "Test", 2002, "Test", "Test")
        self.assertEqual(test, True)

    def test_validate_parameters_book_int_is_str(self):
        test = self.reference_validator.validate_parameters_book("Test", "Test", "Test", "Test", "Test")
        self.assertEqual(test, False)

    def test_validate_parameters_book_str_is_int(self): 
        test = self.reference_validator.validate_parameters_book(2, "Test", 2002, "Test", "Test")
        self.assertEqual(test, False)

    def test_validate_parameters_book_invalid_year(self):
        test = self.reference_validator.validate_parameters_book("Test", "Test", 19922, "Test", "Test")
        self.assertEqual(test, False)

    def test_validate_parameters_book_empty_string(self):
        test = self.reference_validator.validate_parameters_book("", "Test", 2002, "Test", "Test")
        self.assertEqual(test, False)

    def test_validate_parameters_article(self):
        test = self.reference_validator.validate_parameters_article("Test", "Test", 2002, "Test", 2)
        self.assertEqual(test, True)

    def test_validate_parameters_article_int_is_str(self):
        test = self.reference_validator.validate_parameters_article("Test", "Test", "2002", "Test", "Test")
        self.assertEqual(test, False)

    def test_validate_parameters_article_str_is_int(self):
        test = self.reference_validator.validate_parameters_article(2, "Test", 2002, "Test", 2)
        self.assertEqual(test, False)

    def test_validate_parameters_article_invalid_year(self):
        test = self.reference_validator.validate_parameters_article("Test", "Test", 19922, "Test", "Test")
        self.assertEqual(test, False)

    def test_validate_parameters_article_empty_string(self):
        test = self.reference_validator.validate_parameters_article("", "Test", 2002, "Test", "Test")
        self.assertEqual(test, False)

    def test_validate_parameters_inproceedings(self):
        test = self.reference_validator.validate_parameters_inproceedings("Test", "Test", 2002, "Test")
        self.assertEqual(test, True)

    def test_validate_parameters_inproceedings_int_is_str(self):
        test = self.reference_validator.validate_parameters_inproceedings("Test", "Test", "Test", "Test")
        self.assertEqual(test, False)

    def test_validate_parameters_inproceedings_str_is_int(self):
        test = self.reference_validator.validate_parameters_inproceedings(2, "Test", 2002, "Test")
        self.assertEqual(test, False)

    def test_validate_parameters_inproceedings_invalid_year(self):
        test = self.reference_validator.validate_parameters_inproceedings("Test", "Test", 19922, "Test")
        self.assertEqual(test, False)

    def test_validate_parameters_inproceedings_empty_string(self):
        test = self.reference_validator.validate_parameters_inproceedings("", "Test", 2002, "Test")
        self.assertEqual(test, False)


