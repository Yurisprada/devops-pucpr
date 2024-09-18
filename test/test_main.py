import unittest
from src.Main import sum_numbers, average_numbers

class TestMathUtils(unittest.TestCase):

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([3, 4]), 7)
        self.assertEqual(sum_numbers([-1, 1]), 0)

    def test_average_numbers(self):
        # Testando com números positivos
        self.assertAlmostEqual(average_numbers([1, 2, 3, 4]), 2.5)
        # Testando com números negativos
        self.assertAlmostEqual(average_numbers([-1, -2, -3]), -2.0)
        # Testando com uma lista vazia
        self.assertEqual(average_numbers([]), 0)
        # Testando com uma lista de floats
        self.assertAlmostEqual(average_numbers([1.5, 2.5, 3.0]), 2.3333333333333335)

if __name__ == '__main__':
    unittest.main()