import unittest
from unittest.mock import patch
from src.Main import *

class TestZombieDice(unittest.TestCase):

    @patch('builtins.input', return_value='1')
    def test_menu(self, mock_input):
        op = menu()
        self.assertEqual(op, '1')  # Deve retornar '1'

    @patch('builtins.input', return_value='2')
    def test_qtdJogadores(self, mock_input):
        num_jogadores = qtdJogadores()
        self.assertEqual(num_jogadores, 2)  # Deve retornar 2

    @patch('builtins.input', return_value='3')
    def test_qtdJogadores_valido(self, mock_input):
        num_jogadores = qtdJogadores()
        self.assertEqual(num_jogadores, 3)  # Deve retornar 3

    @patch('builtins.input', side_effect=['', 'Player1', 'Player2'])
    def test_cadastro_jogadores(self, mock_input):
        jogadores = cadastro_jogadores()
        self.assertEqual(jogadores, ['Player1', 'Player2'])  # Deve conter os dois nomes válidos

    def test_tuboDados(self):
        tubo = tuboDados()
        self.assertEqual(len(tubo), 13)  # Deve haver 13 dados no tubo
        self.assertEqual(tubo.count(dadoVerde), 6)  # Deve haver 6 dados verdes
        self.assertEqual(tubo.count(dadoAmarelo), 4)  # Deve haver 4 dados amarelos
        self.assertEqual(tubo.count(dadoVermelho), 3)  # Deve haver 3 dados vermelhos

    def test_rollDice(self):
        tubo = tuboDados()
        resultado = rollDice()
        self.assertIn(resultado[0], [dadoVerde, dadoAmarelo, dadoVermelho])  # Deve ser um dos tipos de dados

    def test_rollFace(self):
        dado = rollFace()
        self.assertIn(dado, ['C', 'P', 'T'])  # A face deve ser uma das válidas

    @patch('src.Main.pontAtualC', [0])
    @patch('src.Main.cerebro', [3])
    @patch('src.Main.jogadorAtual', 0)
    def test_pontuacaoC(self, mock_pontAtualC, mock_cerebro, mock_jogadorAtual):
        pontuacaoC()
        self.assertEqual(pontAtualC[0], 3)  # Deve atualizar a pontuação corretamente

    @patch('src.Main.pontAtualP', [0])
    @patch('src.Main.jogadorAtual', 0)
    def test_pontuacaoP(self, mock_pontAtualP, mock_jogadorAtual):
        pontuacaoP()
        self.assertEqual(pontAtualP[0], 1)  # Deve incrementar a pontuação

    @patch('src.Main.pontAtualT', [2])
    @patch('src.Main.cerebro', [5])
    @patch('src.Main.jogadorAtual', 0)
    def test_pontuacaoT(self, mock_pontAtualT, mock_cerebro, mock_jogadorAtual):
        pontuacaoT()
        self.assertEqual(pontAtualT[0], 3)  # Deve incrementar o tiro
        self.assertEqual(cerebro[0], 0)  # Deve zerar os cérebros, pois os tiros chegaram a 3


    @patch('builtins.input', return_value='5')
    def test_menu2(self, mock_input):
        op = menu2()
        self.assertEqual(op, '2')  # Deve retornar '5'

if __name__ == '__main__':
    unittest.main()