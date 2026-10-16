import random

entrada = input("Escreva os nomes dos países (separados por espaço): ")
paises = entrada.split()

if len(paises) > 0:
    vencedor = random.choice(paises)
    print(f"\nO país sorteado para ganhar a Copa é: {vencedor.upper()}!")
else:
    print("Você não digitou nenhum país!")
