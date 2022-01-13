import random as rd

print("\t       Black Jack\n\n\t          Menu\n")

qtdDeJogadores = int(input("\t   Quantos jogadores: "))

jogadores = []
pontosJogadores = []

for x in range(qtdDeJogadores):
    jogadores.append(input(f"\n\tQual o nome do jogador {x + 1}: "))
    pontosJogadores.append(0)
    
baralho = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]
    
while True:
    for x in range(qtdDeJogadores): 
        maisUma = "sim"
        y = 0
        
        rd.shuffle(baralho)
        
        print(f"\nVez do jogador {jogadores[x]}")
        
        while pontosJogadores[x] <= 21:
            
            if baralho[y] == 10 or 1:
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
            
        print(f"O jogador {jogadores[x]} somou {pontosJogadores[x]}")
        
        pontosJogadores[x] = 0

        
   
        
        
    if input("Quer jogar mais uma rodada ? s ou n") == "n":
        break
        
        
    