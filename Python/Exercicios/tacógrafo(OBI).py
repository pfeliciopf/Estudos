n = int(input())

total = 0
tempo_anterior = 0
velocidade_anterior = 0

for _ in range(n):
    t, v = map(int, input().split())
    total += (t - tempo_anterior) * velocidade_anterior
    tempo_anterior = t
    velocidade_anterior = v

print(total)