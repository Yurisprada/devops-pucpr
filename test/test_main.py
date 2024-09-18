import unittest
from unittest.mock import patch
# Importando as funções do arquivo principal (assumindo que está em src/main.py)
from src.Main import *

class TestZombieDice(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['1', '2', 'Jogador1', 'Jogador2', '5', '0'])
    def test_full_game_flow(self, mock_input):
        # 1. Iniciar o jogo
        menu_input = menu(input_func=mock_input)
        self.assertEqual(menu_input, '1')
        
        # 2. Input para quantidade de jogadores
        num_jogadores = qtdJogadores(input_func=mock_input)
        self.assertEqual(num_jogadores, 2)

        # 3. Inputs para nomes dos jogadores
        jogadores = cadastro_jogadores(input_func=mock_input)
        self.assertEqual(jogadores, ['Jogador1', 'Jogador2'])

        # 4. Input para finalizar o jogo
        option = menu2(input_func=mock_input, op2='5')
        self.assertEqual(option, '5')

        # 5. Input para sair da aplicação
        exit_input = menu(input_func=mock_input)
        self.assertEqual(exit_input, '0')


if __name__ == '__main__':
    unittest.main()