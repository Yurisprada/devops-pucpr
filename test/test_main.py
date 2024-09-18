import unittest
from unittest.mock import patch
from src.Main import *

class TestZombieDice(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_menu_start_game(self, mock_input):
        result = menu()
        self.assertEqual(result, '1')  # Ajuste a comparação conforme o esperado em `menu()`