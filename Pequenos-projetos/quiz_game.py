# algumas perguntas são feitas ao usuário e seus acertos
# são contabilizados e mostrados no fim

print("Vamos jogar.", end='\n\n')

print("Você quer jogar?")
play = input("Digite 'sim' para continuar: ")

if play.lower() != 'sim':
    quit()

print("Ok, vamos jogar, então.", end='\n\n')

pontos_jogador = 0
total_perguntas = 4

resposta = input("1. Qual o significado de 'CPU' (em inglês)? ").lower()

if resposta == "central processing unit":
    print("Correto!")
    pontos_jogador += 1
else:
    print("Oops, você errou!")
print()

resposta = input("2. Qual o significado de 'GPU'(em inglês)? ")

if resposta.lower() == "graphics processing unit":
    print("Correto!")
    pontos_jogador += 1
else:
    print("Oops, você errou!")
print()

resposta = input("3. Qual o significado de 'RAM'(em inglês)? ")

if resposta.lower() == "random access memory":
    print("Correto!")
    pontos_jogador += 1
else:
    print("Oops, você errou!")
print()

resposta = input("4. Qual o significado de 'PSU'(em inglês)? ")

if resposta.lower() == "power supply":
    print("Correto!")
    pontos_jogador += 1
else:
    print("Oops, você errou!")
print()

print("Você acertou %d questões de um total de %d!" % (pontos_jogador, total_perguntas))
porcentagem = float( (float(pontos_jogador) / float(total_perguntas)) * 100 )
print("Porcentagem de acertos: %.2f%%" % (porcentagem))