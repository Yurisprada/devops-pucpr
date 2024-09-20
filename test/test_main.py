import unittest
from src.Main import *

class TestMain(unittest.TestCase):

    def test_soma_numeros(self):
        self.assertEqual(soma_numeros([1, 2, 3]), 6)
        self.assertEqual(soma_numeros([-1, 1]), 0)
        self.assertEqual(soma_numeros([]), 0)

    def test_media_numeros(self):
        self.assertAlmostEqual(media_numeros([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(media_numeros([-1, -2, -3]), -2.0)
        self.assertEqual(media_numeros([]), 0)
        self.assertAlmostEqual(media_numeros([1.5, 2.5, 3.0]), 2.3333333333333335)

    def test_produto_numeros(self):
        self.assertEqual(produto_numeros([1, 2, 3]), 6)
        self.assertEqual(produto_numeros([-1, 2]), -2)
        self.assertEqual(produto_numeros([0, 1, 2]), 0)
        self.assertEqual(produto_numeros([]), 1)

    def test_diferenca_numeros(self):
        self.assertEqual(diferenca_numeros([10, 2, 3]), 5)  # 10 - (2 + 3)
        self.assertEqual(diferenca_numeros([-10, -2, -3]), -5)  # -10 - (-2 + -3)
        self.assertEqual(diferenca_numeros([5]), 5)  # Only one number
        self.assertEqual(diferenca_numeros([]), 0)  # Empty list

    def test_numero_maximo(self):
        self.assertEqual(numero_maximo([1, 2, 3, 4]), 4)
        self.assertEqual(numero_maximo([-1, -2, -3]), -1)
        self.assertIsNone(numero_maximo([]))  # Empty list

    def test_numero_minimo(self):
        self.assertEqual(numero_minimo([1, 2, 3, 4]), 1)
        self.assertEqual(numero_minimo([-1, -2, -3]), -3)
        self.assertIsNone(numero_minimo([]))  # Empty list

if __name__ == '__main__':
    unittest.main()