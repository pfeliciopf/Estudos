import random

print("--- JOGO: PEDRA, PAPEL E TESOURA ---")

# O computador escolhe um número de 1 a 3
numero_sorteado = random.randint(1, 3)

if numero_sorteado == 1:
    computador = "pedra"
elif numero_sorteado == 2:
    computador = "papel"
else:
    computador = "tesoura"

# O jogador digita a escolha dele
jogador = input("Digite pedra, papel ou tesoura: ").upper()

print("Você escolheu:", jogador)
print("O computador escolheu:", computador)

# Testando todas as possibilidades uma por uma
if jogador == computador:
    print("Empate!")

# Casos em que o jogador ganha
elif jogador == "pedra" and computador == "tesoura":
    print("Você ganhou!")
elif jogador == "papel" and computador == "pedra":
    print("Você ganhou!")
elif jogador == "tesoura" and computador == "papel":
    print("Você ganhou!")

# Se não foi empate e o jogador não ganhou, ele perdeu
else:
    print("Você perdeu!")
