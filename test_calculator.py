import unittest
from calculator import calculate


class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("2+3"), "5")

    def test_subtraction(self):
        self.assertEqual(calculate("10-4"), "6")

    def test_multiplication(self):
        self.assertEqual(calculate("3*4"), "12")

    def test_division(self):
        self.assertEqual(calculate("10/4"), "2.5")

    def test_chained_operations(self):
        self.assertEqual(calculate("2+3*4"), "14")

    def test_decimal(self):
        self.assertEqual(calculate("1.5+2.5"), "4.0")

    def test_division_by_zero(self):
        self.assertEqual(calculate("1/0"), "Error")

    def test_invalid_expression(self):
        self.assertEqual(calculate("abc"), "Error")

    def test_empty_expression(self):
        self.assertEqual(calculate(""), "Error")


if __name__ == "__main__":
    unittest.main()
