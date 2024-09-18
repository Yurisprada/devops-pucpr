import random
import time

# Cadastro de jogadores #
def qtdJogadores(input_func=input, entrada=None):
    if entrada is None:
        entrada = input_func('Digite o número de jogadores: ')
    try:
        num_jogadores = int(entrada)
        if num_jogadores < 2:
            print("Número de jogadores deve ser pelo menos 2.")
            return qtdJogadores(input_func)
        return num_jogadores
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return qtdJogadores(input_func)

def cadastro_jogadores(input_func=input, entradas=None):
    if entradas is None:
        entradas = [input_func(f'Digite o nome do jogador {i+1}: ') for i in range(qtdJogadores(input_func))]
    jogadores = [entrada for entrada in entradas if entrada]
    return jogadores

# Dados #
dadoVerde = ('C', 'P', 'C', 'T', 'P', 'C')
dadoAmarelo = ('T', 'P', 'C', 'T', 'P', 'C')
dadoVermelho = ('T', 'P', 'T', 'C', 'P', 'T')

# Tubo de dados #
def tuboDados():
    return [
        dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, 
        dadoAmarelo, dadoAmarelo, dadoAmarelo, dadoAmarelo, 
        dadoVermelho, dadoVermelho, dadoVermelho
    ]

# Funções auxiliares #
def rollDice(tubo, jogadorAtual, quantV, quantA, quantR):
    sorteados = []
    dado = random.randint(0, len(tubo) - 1)
    dadoSorteado = tubo[dado]
    if dadoSorteado == dadoVerde:
        quantV[jogadorAtual] = tubo.count(dadoVerde)
        print('Você rolou um dado verde')
    elif dadoSorteado == dadoAmarelo:
        quantA[jogadorAtual] = tubo.count(dadoAmarelo)
        print('Você rolou um dado amarelo')
    else:
        quantR[jogadorAtual] = tubo.count(dadoVermelho)
        print('Você rolou um dado vermelho')
    tubo.remove(dadoSorteado)
    sorteados.append(dadoSorteado)
    return sorteados

def rollFace(dado):
    face = random.randint(0, 5)
    return dado[face]

# Menu #
def menu(input_func=input, op1=None):
    if op1 is None:
        print('1. Iniciar Jogo')
        print('2. Regras')
        print('0. Sair')
        op1 = input_func('Selecione a opção desejada: ')
    return op1

def menu2(input_func=input, op2=None):
    if op2 is None:
        print('1. Rolar dados')
        print('2. Checar pontuação')
        print('3. Dados restantes')
        print('4. Passar turno')
        print('5. Finalizar jogo')
        op2 = input_func('Selecione a opção desejada: ')
    return op2

# Função principal #
def iniciar_jogo(input_func=input):
    tubo = tuboDados()
    tubo_original = list(tubo)
    
    print('Bem vindo ao Zombie Dice')
    op1 = menu(input_func)
    if op1 == '1':
        nomeJogadores = cadastro_jogadores(input_func)
        pontAtualC = [0] * len(nomeJogadores)
        pontAtualP = [0] * len(nomeJogadores)
        pontAtualT = [0] * len(nomeJogadores)
        cerebro = [0] * len(nomeJogadores)
        quantV = [6] * len(nomeJogadores)
        quantA = [4] * len(nomeJogadores)
        quantR = [3] * len(nomeJogadores)
        jogadorAtual = 0
        # Continue com a lógica do jogo como necessário
        return 'Jogo iniciado'
    elif op1 == '2':
        print('Regras do jogo...')
        return 'Regras exibidas'
    elif op1 == '0':
        print('Obrigado por jogar')
        return 'Jogo encerrado'

if __name__ == "__main__":
    iniciar_jogo()
