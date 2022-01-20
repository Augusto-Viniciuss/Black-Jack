from random import shuffle

def imprimeCarta(valorCarta):
    if valorCarta == 10 or valorCarta == 1:
        if valorCarta == 1:
            print(f"\n ____\n|    |\n| Ás |\n|____|")
        else:
            print(f"\n ____\n|    |\n| 10 |\n|____|")
    else:
        if valorCarta == 11:
            print(f"\n ____\n|    |\n| j  |\n|____|")
        elif valorCarta == 12:
            print(f"\n ____\n|    |\n| Q  |\n|____|")
        elif valorCarta == 13:
            print(f"\n ____\n|    |\n| K  |\n|____|")
        else:
            print(f"\n ____\n|    |\n| {valorCarta}  |\n|____|")
    

print('\t\tBlack Jack\n')

try:
    qtdDeJogadores = int(input('Quantos pessoas irão jogar(digite apenas números): '))
except:
    print('Me desculpe só aceito números, por favor reabra o programa e tente novamente :)\n')
else:
    while qtdDeJogadores < 2:
        qtdDeJogadores = int(input('\nDesculpe fui feito para que dois ou mais jogadores competissem entre si.\nPoderia me informar novamente a quantidade de jogadores: '))

    jogadores = []
    jogador = {'Nome': '', 'Rodadas': 0}
    pontosDaRodada = []

    for x in range(qtdDeJogadores):
        jogador['Nome'] = input(f'\n\tQual o nome do jogador {x + 1}: ')
        jogadores.append(jogador.copy())
        pontosDaRodada.append(0)
           
    baralho = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        
    while True:
        for x in range(qtdDeJogadores): 
            y = 0
            
            shuffle(baralho)
            
            print(f'\nVez do jogador {jogadores[x]["Nome"]}')
            
            while pontosDaRodada[x] <= 21:
                imprimeCarta(baralho[y])
                pontosDaRodada[x] += baralho[y]
                y += 1 
                
                if pontosDaRodada[x] <= 21:
                    maisUma = input('\nQuer mais uma carta ? Digite sim ou não: ')
                
                while maisUma != 'sim' and maisUma != 'não':
                    maisUma = input('Não entendi, poderia digitar novamente: ')
                    
                if maisUma != 'sim':
                    break
                
            print(f'\nO jogador {jogadores[x]["Nome"]} somou {pontosDaRodada[x]} pontos')
            
            if pontosDaRodada[x] > 21:
                pontosDaRodada[x] = 0
                
        maiorValor = max(pontosDaRodada)
        jogadorComOValorMax = -1
        jogadoresComOValorMax = 0
    
        for x in range(qtdDeJogadores):
            if maiorValor == pontosDaRodada[x]:
                jogadorComOValorMax = x
                jogadoresComOValorMax += 1
                
        if jogadoresComOValorMax > 1:
            print('\nEssa rodada empatou.')
        else:
            print(f'\nO ganhador da rodada foi o jogador {jogadores[jogadorComOValorMax]["Nome"]} que somou {pontosDaRodada[jogadorComOValorMax]} pontos.')
            
        jogadores[jogadorComOValorMax]['Rodadas'] += 1
        
        outraRodada = input('\nQuer jogar mais uma rodada ? sim ou não: ')
        
        while outraRodada != 'sim' and outraRodada != 'não':
            outraRodada = input('Não entendi, poderia digitar novamente: ')

        if outraRodada == 'não':
            break
        
        for x in range(qtdDeJogadores):
            pontosDaRodada[x] = 0

    for z in range(qtdDeJogadores):
        print(f'\nO jogador {jogadores[z]["Nome"]} ganhou {jogadores[z]["Rodadas"]} rodada(s) nessa partida')
    print()
