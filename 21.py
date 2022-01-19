from random import shuffle

print("\t\tBlack Jack\n")

qtdDeJogadores = int(input("Quantos pessoas irão jogar(digite apenas números): "))

while qtdDeJogadores < 2:
    qtdDeJogadores = int(input("\nDesculpe fui feito para que dois ou mais jogadores competissem entre si.\nPoderia me informar novamente a quiantidade de jogadores: "))

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
            
            if pontosJogadores[x] <= 21:
                maisUma = input("\nQuer mais uma carta ? Digite sim ou não: ")
            
            while maisUma != "sim" and maisUma != "não":
                maisUma = input("Não entendi, poderia digitar novamente: ")
                
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
        print("\nEssa rodada empatou.")
    else:
        print(f"\nO ganhador da rodada foi o jogador {jogadores[jogadorComOValorMax]} que somou {pontosJogadores[jogadorComOValorMax]} pontos.")
        
    rodadasGanhas[jogadorComOValorMax] += 1
    
    outraRodada = input("\nQuer jogar mais uma rodada ? sim ou não: ")
    
    while outraRodada != "sim" and outraRodada != "não":
        outraRodada = input("Não entendi, poderia digitar novamente: ")

    if outraRodada == "não":
        break
    
    for x in range(qtdDeJogadores):
        pontosJogadores[x] = 0

for z in range(qtdDeJogadores):
    print(f"\nO jogador {jogadores[z]} ganhou {rodadasGanhas[z]} rodada(s) nessa partida")
