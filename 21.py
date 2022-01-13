print("\t       Black Jack\n\n\t          Menu\n")

qtdDeJogadores = int(input("\t   Quantos jogadores: "))

Jogadores = []

for x in range(qtdDeJogadores):
    Jogadores.append(input(f"\n\tQual o nome do jogador {x + 1}: "))
    
