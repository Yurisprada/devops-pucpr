import unittest
from unittest.mock import patch
from src import *

class TestZombieDice(unittest.TestCase):
    
    # Testando iniciar o jogo com a opção 1 no menu
    @patch('builtins.input', side_effect=['1'])  # Simulando escolha da opção 1 (Iniciar Jogo)
    def test_menu_iniciar_jogo(self, mock_input):
        op1 = menu()
        self.assertEqual(op1, '1')

    # Testando finalizar o jogo com a opção 0 no menu
    @patch('builtins.input', side_effect=['0'])  # Simulando escolha da opção 0 (Finalizar Jogo)
    def test_menu_finalizar_jogo(self, mock_input):
        op1 = menu()
        self.assertEqual(op1, '0')


if __name__ == '__main__':
    unittest.main()