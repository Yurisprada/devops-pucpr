import unittest
from unittest.mock import patch
from src.Main import *

class TestZombieDice(unittest.TestCase):

    def test_menu():
    # Simula a entrada do usuário como '1'
        with patch('builtins.input', return_value='1'):
            op1 = menu()
        assert op1 == '1'

    @patch('builtins.input', side_effect=['1'])
    def test_menu_start_game(self, mock_input):
        result = menu()
        self.assertEqual(result, '1')  # Ajuste a comparação conforme o esperado em `menu()`


if __name__ == '__main__':
    unittest.main()