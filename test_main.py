import unittest
from unittest.mock import patch

from Main import (
    qtdJogadores, cadastro_jogadores, tuboDados, rollDice, rollFace,
    pontuacaoC, pontuacaoP, pontuacaooT, scoreAtual, scoreCheck,
    dadosRestantes, winner, removerVencedor
)

class TestZombieDice(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['1', 'abc', '2'])  # Simula entradas inválidas e depois uma válida
    def test_qtdJogadores(self, mock_input):
        num_jogadores = qtdJogadores()
        self.assertEqual(num_jogadores, 2)  # Deve retornar 2, que é a primeira entrada válida

    @patch('builtins.input', side_effect=['3'])
    def test_qtdJogadores_valido(self, mock_input):
        num_jogadores = qtdJogadores()
        self.assertEqual(num_jogadores, 3)  # Deve retornar 3

@patch('builtins.input', side_effect=['', 'Player1', 'Player2'])  # Simula uma entrada inválida e duas válidas
def test_cadastro_jogadores(self, mock_input):
    jogadores = cadastro_jogadores()
    self.assertEqual(jogadores, ['Player1', 'Player2'])  # Deve conter os dois nomes válidos

def test_tuboDados(self):
    tubo = tuboDados()
    self.assertEqual(len(tubo), 13)  # Deve haver 13 dados no tubo
    self.assertEqual(tubo.count(dadoVerde), 6)  # Deve haver 6 dados verdes
    self.assertEqual(tubo.count(dadoAmarelo), 4)  # Deve haver 4 dados amarelos
    self.assertEqual(tubo.count(dadoVermelho), 3)  # Deve haver 3 dados vermelhos

@patch('random.randint', return_value=0)  # Força o dado a ser sempre o primeiro do tubo
def test_rollDice(self, mock_randint):
    tubo = tuboDados()
    resultado = rollDice()
    self.assertIn(resultado[0], [dadoVerde, dadoAmarelo, dadoVermelho])  # Deve ser um dos tipos de dados

@patch('random.randint', return_value=0)
def test_rollFace(self, mock_randint):
    dado = rollFace()
    self.assertIn(dado, ['C', 'P', 'T'])  # A face deve ser uma das válidas

def test_pontuacaoC(self):
    global pontAtualC, cerebro, jogadorAtual
    pontAtualC = [0]
    cerebro = [3]
    jogadorAtual = 0
    pontuacaoC()
    self.assertEqual(pontAtualC[0], 3)  # Deve atualizar a pontuação corretamente

def test_pontuacaoP(self):
    global pontAtualP, jogadorAtual
    pontAtualP = [0]
    jogadorAtual = 0
    pontuacaoP()
    self.assertEqual(pontAtualP[0], 1)  # Deve incrementar a pontuação

def test_pontuacaoT(self):
    global pontAtualT, cerebro, jogadorAtual
    pontAtualT = [2]
    cerebro = [5]
    jogadorAtual = 0
    pontuacaooT()
    self.assertEqual(pontAtualT[0], 3)  # Deve incrementar o tiro
    self.assertEqual(cerebro[0], 0)  # Deve zerar os cérebros, pois os tiros chegaram a 3

if __name__ == '__main__':
    unittest.main()