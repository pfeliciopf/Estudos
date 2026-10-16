N = int(input())

ranking = [0] * (N + 1)

for posicao_atual in range(1, N + 1):
    atleta = int(input())
    ranking[atleta] = posicao_atual

for i in range(1, N + 1):
    print(ranking[i])
    