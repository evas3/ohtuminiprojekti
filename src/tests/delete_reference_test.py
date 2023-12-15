import unittest
from delete_reference import DeleteReference

class TestDeleteReference(unittest.TestCase):
    def setUp(self):
        self.delete_reference = DeleteReference()
    
    def test_key_not_found(self):
        test = self.delete_reference.key_check("c", [["a"], ["b"]])
        self.assertEqual(test, [1, -1])

    def test_key_found(self):
        test = self.delete_reference.key_check("a", [["a"], ["b"]])
        self.assertEqual(test, [0, 1])

    def test_file_not_found(self):
        test = self.delete_reference.delete_reference("a", 0, 0)
        self.assertEqual(test, False)

    def test_delete_shortform_file_not_found(self):
        test = self.delete_reference.delete_shortform("a", 0)
        self.assertEqual(test, False)
