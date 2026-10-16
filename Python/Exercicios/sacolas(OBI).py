#prova 2025 

n, s= list(map(int, input().split()))
pesos = map(int, input().split())

sacolas=1
peso_atual=0

for peso in pesos:
    if peso_atual + peso <= s:
        peso_atual += peso
    else:
        sacolas += 1
        peso_atual = peso

print (sacolas)