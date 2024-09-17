import random
import time

#Cadastro de jogadores#

def qtdJogadores():
    numJog = 0
    while numJog<2:
        try:
            numJog = int(input('Qual a quantidade de jogadores: '))
            if numJog <2:
                print('Mínimo 2 Jogadores')
            else:
                print('Bom jogo')
        except:
            print('Valor invalido')
    return numJog

def cadastro_jogadores():
    nomeJog =[]
    numJog = qtdJogadores()
    i = 1
    while i <= numJog:
        jogador = input('Digite o nome do jogador %s: '%i)
        if jogador == '':
            print('Valor invalido')
        else:
            i = i + 1
            print('Jogador registrado com sucesso')
            nomeJog.append(jogador)
    return nomeJog

#Dados#

dadoVerde = ('C', 'P', 'C', 'T', 'P', 'C')
dadoAmarelo = ('T', 'P', 'C', 'T', 'P', 'C')
dadoVermelho = ('T', 'P', 'T', 'C', 'P', 'T')

#Tubo#

def tuboDados():
    tubo =  [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoAmarelo, dadoAmarelo, dadoAmarelo,
            dadoAmarelo, dadoVermelho, dadoVermelho, dadoVermelho]
    return tubo

tubo = tuboDados()
tubo2 = [dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoVerde, dadoAmarelo, dadoAmarelo, dadoAmarelo,
            dadoAmarelo, dadoVermelho, dadoVermelho, dadoVermelho]

#Sortear dados e faces#

def rollDice():
    sorteados = []
    dado = random.randint(0,len(tubo)-1)
    dadoSorteado = tubo[dado]
    if dadoSorteado == dadoVerde:
        quantV[jogadorAtual] = tubo.count(dadoVerde)
        print ('Você rolou um dado verde')
        tubo.remove(dadoSorteado)
    elif dadoSorteado == dadoAmarelo:
        quantA[jogadorAtual] = tubo.count(dadoAmarelo)
        print('Você rolou um dado amarelo')
        tubo.remove(dadoSorteado)
    else:
        quantR[jogadorAtual] = tubo.count(dadoVermelho)
        print('Você rolou um dado vermelho')
        tubo.remove(dadoSorteado)
    sorteados.append(dadoSorteado)
    return sorteados

def rollFace():
    dado = rollDice()
    for dados in dado:
        face = random.randint(0,5)
    return dados[face]

#Somatizar pontuação#

def pontuaçãoC():
    pontAtualC[jogadorAtual] = pontAtualC[jogadorAtual] + cerebro[jogadorAtual]
    return pontAtualC[jogadorAtual]

def pontuaçãoP():
    pontAtualP[jogadorAtual] = pontAtualP[jogadorAtual] + 1
    return pontAtualP[jogadorAtual]

def pontuaçãoT():
    pontAtualT[jogadorAtual] = pontAtualT[jogadorAtual] + 1
    if pontAtualT[jogadorAtual] >= 3:
        cerebro = 0
    return pontAtualT[jogadorAtual]

#Checar o placar#

def scoreAtual():
    print('----------------------------------\n'
          'Possui atualmente: \nCérebros: ',cerebro[jogadorAtual],'\nPassos: ',pontAtualP[jogadorAtual],'\nTiros: ',
          pontAtualT[jogadorAtual])

def scoreCheck():
    for i in range(len(nomeJogadores)):
        print(nomeJogadores[i], 'possui', (pontAtualC[i]+cerebro[i]), 'cérebros em ', turnAtual[i], 'rodadas')

#Checar dados restantes#

def dadosRestantes():
    for i in range(1):
        print('Os dados restantes são:\n{} Verde\n{} Amarelo\n{} Vermelho'.format(quantV[i],quantA[i],quantR[i]))

#Vencedor#

def winner():
    i = 0
    cerebros = 0
    vencedor = 0
    while i < len(nomeJogadores):
        if cerebros < pontAtualC[i]:
            cerebros = pontAtualC[i]
            vencedor = i
        i = i + 1
    return vencedor

lista_vencedor = []
cerebro_vencedor = []
turno_vencedor = []

#Anunciar jogadores eliminados#

def turnosRestantes():
    i = 0
    for i in range(len(nomeJogadores)):
        if turnAtual[i] <= turnAtual[vencedor]:
            print(nomeJogadores[i], 'tem até o final da rodada para vencer')
        elif turnAtual[i] > turnAtual[vencedor]:
            print(nomeJogadores[i], ' esta eliminado')

#Remover Vencedor#

def removerVencedor():
    nomeJogadores.pop(vencedor)
    pontAtualC.pop(vencedor)
    pontAtualP.pop(vencedor)
    pontAtualT.pop(vencedor)
    quantV.pop(vencedor)
    quantA.pop(vencedor)
    quantR.pop(vencedor)
    cerebro.pop(vencedor)

#Menu#

def menu():
    print('1.Iniciar Jogo')
    print('2.Regras')
    print('0.Sair')
    op1 = input('Selecione a opção desejada: ')
    return op1

def menu2():
    print('1.Rolar dados')
    print('2.Checar pontuação')
    print('3.Dados restantes')
    print('4.Passar turno')
    print('5.Finalizar jogo')
    op2 = input('Selecione a opção desejada: ')
    return op2

#Zombie Dice#

comecar = 's'
while comecar == 's':
    print('Bem vindo a Zombie Dice')
    op1 = menu()
    if op1 == '1':
        nomeJogadores = cadastro_jogadores()
        pontAtualC = [0] * len(nomeJogadores)
        pontAtualP = [0] * len(nomeJogadores)
        pontAtualT = [0] * len(nomeJogadores)
        turnAtual = [1] * len(nomeJogadores)
        quantV = [6] * len(nomeJogadores)
        quantA = [4] * len(nomeJogadores)
        quantR = [3] * len(nomeJogadores)
        cerebro = [0] * len(nomeJogadores)
        jogadorAtual = 0
        reroll = 's'
        while reroll == 's':
            print('---------------------------------------\nJogador ',nomeJogadores[jogadorAtual])
            print('Rodada ',turnAtual[jogadorAtual],'\n------------------------------------------')
            op2 = menu2()
            if op2 == '1':
                for i in range(3):
                    print('Rolando dado...')
                    time.sleep(1)
                    face = rollFace()
                    if face == 'C':
                        print('Com a face: ',face)
                        cerebro[jogadorAtual] += 1
                    elif  face == 'P':
                        print('Com a face: ',face)
                        pontuaçãoP()
                    else:
                        print('Com a face: ',face)
                        pontuaçãoT()
                        tiro = pontAtualT[jogadorAtual]
                        if tiro >= 3:
                            print('Você perdeu o turno e os cérebros dessa rodada')
                            cerebro[jogadorAtual] = 0
                            pontAtualT[jogadorAtual] = 0
                            pontAtualP[jogadorAtual] = 0
                            turnAtual[jogadorAtual] += 1
                            jogadorAtual = jogadorAtual + 1
                            if jogadorAtual >= len(nomeJogadores):
                                jogadorAtual = 0
                            time.sleep(1)
                            break
                scoreAtual()
            if (cerebro[jogadorAtual] + pontAtualC[jogadorAtual]) >= 13 or pontAtualC[jogadorAtual] >= 13:
                pontuaçãoC()
                vencedor = winner()
                print('---------------------------------------------\n'
                      'O vencedor é: ', nomeJogadores[vencedor], 'em ',turnAtual[vencedor],'rodadas\n-------------------'
                                                                                           '--------------------------')
                novoJogo = ''
                while novoJogo != 's':
                    novoJogo = input('Deseja começar uma nova partida? s/n: ').lower()
                    if novoJogo == 's':
                        nomeJogadores.insert(0,nomeJogadores[vencedor])
                        pontAtualC = [0] * len(nomeJogadores)
                        pontAtualP = [0] * len(nomeJogadores)
                        pontAtualT = [0] * len(nomeJogadores)
                        turnAtual = [1] * len(nomeJogadores)
                        quantV = [6] * len(nomeJogadores)
                        quantA = [4] * len(nomeJogadores)
                        quantR = [3] * len(nomeJogadores)
                        cerebro = [0] * len(nomeJogadores)
                        jogadorAtual = 0
                        vencedor += 1
                        removerVencedor()
                        turnAtual.pop(vencedor)
                        print('Recomeçando jogo...')
                        time.sleep(1)
                        break
                    elif novoJogo == 'n':
                        reroll = 'n'
                        break
                    else:
                        print('Valor inválido.Digite novamente')
            if op2 == '2':
                scoreCheck()
            if op2 == '3':
                dadosRestantes()
            if op2 == '4':
                pontuaçãoC()
                cerebro[jogadorAtual] = 0
                pontAtualT[jogadorAtual] = 0
                pontAtualP[jogadorAtual] = 0
                turnAtual[jogadorAtual] += 1
                jogadorAtual = jogadorAtual + 1
                if jogadorAtual >= len(nomeJogadores):
                    jogadorAtual = 0
            elif len(tubo) <= 3:
                tubo = list.copy(tubo2)
            if op2 == '5':
                pontuaçãoC()
                vencedor = winner()
                print('---------------------------------------------\n'
                      'O vencedor é: ', nomeJogadores[vencedor], 'com :',cerebro[vencedor],'cerébros, em', turnAtual[vencedor],
                      'rodadas\n---------------------------------------------')
                print('Obrigado por jogar!!!')
                print('Finalizando jogo...')
                time.sleep(1)
                break
    if op1 == '2':
        print('----------------------------------------'
              '-\nEste jogo inclui estas regras\n1.13 dados e um tubo para guardá-los.\n'
              '2.Dois ou mais jogadores podem jogar.\n3.O primeiro jogador será aquele que venceu a última partida ou a '
              'pessoa que falar “Céééééérebros” da maneira mais zumbi possível.')
        print('4.No seu turno, agite o tubo e pegue 3 dados, sem olhar.Role os dados.\nCada um deles representa uma pobre'
              ' vítima a ser atacada. Os dados vermelhos são os mais difíceis.Os verdes são os mais fáceis e os amarelos'
              ' são médios.')
        print('5.Os dados possuem 3 faces: Cérebros, Espingardas e Passos')
        print('6.Se você tiver 3 espingardas virada para cima na mesa, em qualquer momento, seu turno acabou')
        print('Caso contrário, você pode optar por parar e marcar pontos ou continuar')
        print('7.Se você decidir parar, marque 1 ponto para cada cérebro que você tem, e coloque todos os dados de volta'
              'no tubo')
        print('8.Se você escolher continuar, você não devolve os dados ao tubo')
        print('9.Jogue até alguém chegar a 13 Cérebros. Termine a rodada. Todos devem jogar o mesmo número de turnos')
        print('10.Quem tiver devorado mais cérebros até o final dessa rodada é o vencedor.')
        print('Se houver empate, os líderes jogam uma rodada de desempate\n-------------------------------------------')
    if op1 == '0':
        print('Obrigado por jogar')
        break