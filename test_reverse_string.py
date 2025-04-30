import unittest
from ReverseString import reverse_string

class TestReverseString(unittest.TestCase):
    def test_regular_string(self):
        # Test reversing a regular string
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty_string(self):
        # Test reversing an empty string
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        # Test reversing a single character
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self):
        # Test reversing a palindrome (should be the same)
        self.assertEqual(reverse_string("madam"), "madam")

    def test_whitespace(self):
        # Test reversing a string with spaces
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

if __name__ == "__main__":
    unittest.main()