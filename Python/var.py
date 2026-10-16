jogadores = []

# Time A
for i in range(11):
    x = int(input())
    jogadores.append(["A", x])

# Time B
for i in range(11):
    x = int(input())
    jogadores.append(["B", x])

# Ordena pela posição
jogadores.sort(key=lambda x: x[1])

cont_a = 0

for jogador in jogadores:
    if jogador[0] == "A":
        cont_a += 1
    else:  # Encontrou o primeiro B
        if cont_a < 2:
            print("IMPEDIMENTO")
        else:
            print("SEM IMPEDIMENTO")
        break