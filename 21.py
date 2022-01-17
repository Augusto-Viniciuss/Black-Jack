from random import shuffle

print("\t          Black Jack\n\n\t             Menu\n")

qtdDeJogadores = int(input("\t      Quantos jogadores: "))

jogadores = []
pontosJogadores = []
rodadasGanhas = []

for x in range(qtdDeJogadores):
    jogadores.append(input(f"\n\tQual o nome do jogador {x + 1}: "))
    pontosJogadores.append(0)
    rodadasGanhas.append(0)
    
baralho = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]
    
while True:
    for x in range(qtdDeJogadores): 
        maisUma = "sim"
        y = 0
        
        shuffle(baralho)
        
        print(f"\nVez do jogador {jogadores[x]}")
        
        while pontosJogadores[x] <= 21:
            
            if baralho[y] == 10 or baralho[y] == 1:
                if baralho[y] == 1:
                    print(f"\n ____\n|    |\n| Ás |\n|____|")
                else:
                    print(f"\n ____\n|    |\n| 10 |\n|____|")
            else:
                if baralho[y] == 11:
                    print(f"\n ____\n|    |\n| j  |\n|____|")
                elif baralho[y] == 12:
                    print(f"\n ____\n|    |\n| Q  |\n|____|")
                elif baralho[y] == 13:
                    print(f"\n ____\n|    |\n| K  |\n|____|")
                else:
                    print(f"\n ____\n|    |\n| {baralho[y]}  |\n|____|")
            
            pontosJogadores[x] += baralho[y]
            
            y += 1 
            
            maisUma = input("\nQuer mais uma carta ? Digite sim ou não: ")
            
            if maisUma != "sim":
                break
            
        print(f"\nO jogador {jogadores[x]} somou {pontosJogadores[x]} pontos")
        
        if pontosJogadores[x] > 21:
            pontosJogadores[x] = 0

    maiorValor = max(pontosJogadores)
    jogadorComOValorMax = -1
    jogadoresComOValorMax = 0
   
    for x in range(qtdDeJogadores):
        if maiorValor == pontosJogadores[x]:
            jogadorComOValorMax = x
            jogadoresComOValorMax += 1
            
    if jogadoresComOValorMax > 1:
        print("\nDois ou mais jogadores tiraram o mesmo numero que foi o ganhador então essa rodada empatou.")
    else:
        print(f"\nO ganhador da rodada foi o jogador {jogadores[jogadorComOValorMax]} que somou {pontosJogadores[jogadorComOValorMax]} pontos.")
        
    rodadasGanhas[jogadorComOValorMax] += 1

    if input("\nQuer jogar mais uma rodada ? s ou n: ") == "n":
        break
    
    for x in range(qtdDeJogadores):
        pontosJogadores[x] = 0

for z in range(qtdDeJogadores):
    print(f"\nO jogador {jogadores[z]} ganhou {rodadasGanhas[z]} rodada(s) nessa partida")
