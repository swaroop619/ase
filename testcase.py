def add_numbers(num1, num2):
    return num1 + num2

# Test case for add_numbers function
import unittest

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -4), -6)
        
    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(0, 0), 0)
        
    def test_add_floats(self):
        self.assertAlmostEqual(add_numbers(2.5, 3.1), 5.6)

if __name__ == "__main__":
    unittest.main()
