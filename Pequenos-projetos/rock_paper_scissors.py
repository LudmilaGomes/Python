import random
import os

os.system('cls')

vitorias_jogador = 0
vitorias_computador = 0
opcoes = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("Escreva pedra/papel/tesoura ou q para sair: ").lower()
    print()

    if jogador == 'q':
        break
    
    if jogador not in opcoes:
        continue

    numero_aleatorio = random.randint(0, 2)
    # pedra: 0, papel: 1, tesoura: 2

    computador = opcoes[numero_aleatorio]

    print("Computador: %s .VS. Jogador: %s" % (computador, jogador))

    if jogador == computador:
        print("Empate! Ambos pontuam.")
        vitorias_computador += 1
        vitorias_jogador += 1

    if jogador == "pedra":
        if computador == "papel":
            print("O Computador ganhou!!!")
            vitorias_computador += 1
        if computador == "tesoura":
            print("O Jogador ganhou!!!")
            vitorias_jogador += 1

    if jogador == "papel":
        if computador == "pedra":
            print("O Jogador ganhou!!!")
            vitorias_jogador += 1
        if computador == "tesoura":
            print("O Computador ganhou!!!")
            vitorias_computador += 1

    if jogador == "tesoura":
        if computador == "papel":
            print("O Jogador ganhou!!!")
            vitorias_jogador += 1
        if computador == "pedra":
            print("O Computador ganhou!!!")
            vitorias_computador += 1

    print()

print("Computador: %d .VS. Jogador: %d" % (vitorias_computador, vitorias_jogador))
print("Até a próxima!")