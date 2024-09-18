import unittest
from unittest.mock import patch
from src import *

class TestZombieDice(unittest.TestCase):
    
    # Testando iniciar o jogo com a opção 1 no menu
    @patch('builtins.input', side_effect=['1'])  # Simulando escolha da opção 1 (Iniciar Jogo)
    def test_menu_iniciar_jogo(self, mock_input):
        op1 = menu()
        self.assertEqual(op1, '1')

    # Testando a função qtdJogadores
    @patch('builtins.input', side_effect=['3'])
    def test_qtd_jogadores_valido(self, mock_input):
        self.assertEqual(qtdJogadores(), 3)

    @patch('builtins.input', side_effect=['1', '3'])
    def test_qtd_jogadores_invalido(self, mock_input):
        self.assertEqual(qtdJogadores(), 3)  # Deve ignorar o 1 e aceitar o 3 como válido

    @patch('builtins.input', side_effect=['abc', '2'])
    def test_qtd_jogadores_entrada_invalida(self, mock_input):
        self.assertEqual(qtdJogadores(), 2)

    # Testando a função cadastro_jogadores
    @patch('builtins.input', side_effect=['Alice', 'Bob'])
    def test_cadastro_jogadores(self, mock_input):
        jogadores = cadastro_jogadores()
        self.assertEqual(jogadores, ['Alice', 'Bob'])

    # Testando a função rollDice
    @patch('random.randint', return_value=0)  # Simulando o primeiro dado do tubo
    def test_roll_dice(self, mock_randint):
        global tubo
        tubo = [('C', 'P', 'C', 'T', 'P', 'C')] * 13  # Reiniciando o tubo para os testes
        sorteados = rollDice()
        self.assertEqual(sorteados, [('C', 'P', 'C', 'T', 'P', 'C')])
        self.assertEqual(len(tubo), 12)  # Verificando se o dado foi removido do tubo

    # Testando a função scoreCheck
    def test_score_check(self):
        global nomeJogadores, pontAtualC, cerebro, turnAtual
        nomeJogadores = ['Alice', 'Bob']
        pontAtualC = [3, 5]
        cerebro = [1, 2]
        turnAtual = [1, 2]

        with patch('builtins.print') as mock_print:
            scoreCheck()
            mock_print.assert_any_call('Alice possui 4 cérebros em 1 rodadas')
            mock_print.assert_any_call('Bob possui 7 cérebros em 2 rodadas')

    # Testando a função winner
    def test_winner(self):
        global nomeJogadores, pontAtualC
        nomeJogadores = ['Alice', 'Bob', 'Charlie']
        pontAtualC = [3, 8, 5]
        self.assertEqual(winner(), 1)  # Bob deve ser o vencedor (índice 1)

    # Testando finalizar o jogo com a opção 0 no menu
    @patch('builtins.input', side_effect=['0'])  # Simulando escolha da opção 0 (Finalizar Jogo)
    def test_menu_finalizar_jogo(self, mock_input):
        op1 = menu()
        self.assertEqual(op1, '0')


if __name__ == '__main__':
    unittest.main()