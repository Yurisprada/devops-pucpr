import pytest
import random
from src.Main import (
    qtdJogadores, cadastro_jogadores, tuboDados, rollDice, rollFace,
    pontuaçãoC, pontuaçãoP, pontuaçãoT, dadosRestantes, winner,
    turnosRestantes, removerVencedor
)

@pytest.fixture
def setup_game():
    # Fixture para preparar o ambiente de teste
    global nomeJogadores, pontAtualC, pontAtualP, pontAtualT, turnAtual, quantV, quantA, quantR, cerebro, jogadorAtual
    nomeJogadores = ['Player1', 'Player2']
    pontAtualC = [0, 0]
    pontAtualP = [0, 0]
    pontAtualT = [0, 0]
    turnAtual = [1, 1]
    quantV = [6, 6]
    quantA = [4, 4]
    quantR = [3, 3]
    cerebro = [0, 0]
    jogadorAtual = 0

def test_qtdJogadores_valido(setup_game):
    result = qtdJogadores('3')
    assert result == 3

def test_qtdJogadores_invalido(setup_game):
    result = qtdJogadores('abc')
    assert result == 2  # Porque o retorno padrão é 2 em caso de erro, ajustado conforme a lógica real

def test_cadastro_jogadores(setup_game):
    entradas = ['Player1', 'Player2']
    result = cadastro_jogadores(entradas)
    assert result == ['Player1', 'Player2']

def test_tuboDados(setup_game):
    tubo = tuboDados()
    assert len(tubo) == 13
    assert tubo.count(('C', 'P', 'C', 'T', 'P', 'C')) == 6
    assert tubo.count(('T', 'P', 'C', 'T', 'P', 'C')) == 4
    assert tubo.count(('T', 'P', 'T', 'C', 'P', 'T')) == 3

def test_rollDice(setup_game):
    random.seed(0)  # Para tornar o teste reprodutível
    result = rollDice()
    assert len(result) == 1  # Espera-se um dado sorteado
    assert result[0] in [dadoVerde, dadoAmarelo, dadoVermelho]

def test_rollFace(setup_game):
    random.seed(0)
    result = rollFace()
    assert result in ['C', 'P', 'T']

def test_pontuaçãoC(setup_game):
    cerebro[0] = 3
    result = pontuaçãoC()
    assert result == 3

def test_pontuaçãoP(setup_game):
    pontAtualP[0] = 0
    result = pontuaçãoP()
    assert result == 1

def test_pontuaçãoT(setup_game):
    pontAtualT[0] = 2
    result = pontuaçãoT()
    assert result == 3
    assert cerebro[0] == 0

def test_dadosRestantes(setup_game):
    result = dadosRestantes()
    assert result == 'Os dados restantes são:\n6 Verde\n4 Amarelo\n3 Vermelho'

def test_winner(setup_game):
    pontAtualC = [13, 10]
    result = winner()
    assert result == 0

def test_turnosRestantes(setup_game):
    turnAtual = [2, 1]
    result = turnosRestantes()
    assert result == 'Player1 tem até o final da rodada para vencer\nPlayer2 está eliminado'

def test_removerVencedor(setup_game):
    removerVencedor()
    assert len(nomeJogadores) == 1
    assert nomeJogadores[0] == 'Player2'