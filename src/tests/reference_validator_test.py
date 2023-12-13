import unittest
from reference_validator import ValidateParameters

class TestReferenceValidator(unittest.TestCase):
    def setUp(self):
        self.reference_validator = ValidateParameters()

    def test_validators_parameters_are_correct(self):
        test = self.reference_validator.validate_parameters("Testi Testaaja", "1992")
        self.assertEqual(test, True)

    def test_validators_parameters_year_is_not_number(self):
        test = self.reference_validator.validate_parameters("Testi Testaaja", "Testi")
        self.assertEqual(test, False)

    def test_validators_parameters_author_is_number(self): 
        test = self.reference_validator.validate_parameters("1992" , "1993")
        self.assertEqual(test, False)

    def test_validators_parameters_invalid_year(self):
        test = self.reference_validator.validate_parameters("Testi Testaaja", "19922")
        self.assertEqual(test, False)

    def test_validators_parameters_empty_input_author(self):
        test = self.reference_validator.validate_parameters("", "1992")
        self.assertEqual(test, False)

    def test_validators_parameters_empty_input_year(self):
        test = self.reference_validator.validate_parameters("Testi Testaaja", "")
        self.assertEqual(test, False)
