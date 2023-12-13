import unittest
from reference_validator import ValidateParameters

class TestReferenceValidator(unittest.TestCase):
    def setUp(self):
        self.reference_validator = ValidateParameters()

    def test_author_validator_parameter_is_correct(self):
        test = self.reference_validator.validate_parameters_author("Pekka Python")
        self.assertEqual(test, True)

    def test_author_validator_is_not_empty(self):
        test = self.reference_validator.validate_parameters_author("")
        self.assertEqual(test, False)

    def test_author_validator_parameter_is_not_number(self):
        test = self.reference_validator.validate_parameters_author("1992")
        self.assertEqual(test, False)

    def test_author_validator_parameter_does_not_contain_letters_and_numbers(self):
        test = self.reference_validator.validate_parameters_author("Pekka Python 1992")
        self.assertEqual(test, False)
    
    def test_year_validator_parameter_is_correct(self):
        test = self.reference_validator.validate_parameters_year("1992")
        self.assertEqual(test, True)

    def test_year_validator_is_not_empty(self):
        test = self.reference_validator.validate_parameters_year("")
        self.assertEqual(test, False)

    def test_year_validator_parameter_has_invalid_year(self):
        test = self.reference_validator.validate_parameters_year("19922")
        self.assertEqual(test, False)

    def test_year_validator_parameter_is_not_letters(self):
        test = self.reference_validator.validate_parameters_year("Python")
        self.assertEqual(test, False)
