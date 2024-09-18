import unittest
from unittest.mock import patch
from src.Main import *

class TestZombieDice(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_menu(self, mock_input):
        op = menu()
        self.assertEqual(op, '1')  # Deve retornar '1'

    @patch('builtins.input', return_value='5')
    def test_menu2(self, mock_input):
        op = menu2()
        self.assertEqual(op, '2')  # Deve retornar '5'

if __name__ == '__main__':
    unittest.main()