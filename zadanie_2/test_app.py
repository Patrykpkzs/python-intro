import unittest
from app import validate_email, calculate_area, get_even_numbers, convert_date, check_palindrome

class AppTests(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(validate_email("user@example.com"))
        self.assertFalse(validate_email("wrong-email"))
        self.assertFalse(validate_email("test@.com"))

    def test_calculate_area(self):
        self.assertEqual(calculate_area(3, 4), 12)
        self.assertRaises(ValueError, calculate_area, -1, 5)
        self.assertEqual(calculate_area(0, 7), 0)

    def test_get_even_numbers(self):
        self.assertEqual(get_even_numbers([1, 2, 3, 4]), [2, 4])
        self.assertEqual(get_even_numbers([1, 3, 5]), [])
        self.assertEqual(get_even_numbers([]), [])

    def test_convert_date(self):
        self.assertEqual(convert_date("2025-03-20"), "20.03.2025")
        self.assertRaises(ValueError, convert_date, "20-03-2025")

    def test_check_palindrome(self):
        self.assertTrue(check_palindrome("Racecar"))
        self.assertFalse(check_palindrome("Python"))
        self.assertTrue(check_palindrome("Madam, in Eden I'm Adam"))

if __name__ == 'main':
    unittest.main()