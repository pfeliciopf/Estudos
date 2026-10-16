#Prova 2023 fase 2

N = int(input())
G = int(input())
M = int(input())

total = G * 8 + M * 6
sobra = total - min(N, total)

print(sobra)