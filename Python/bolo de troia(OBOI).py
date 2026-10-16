n = int(input())

andares=[]
for _ in range(n):
    x, y = map(int, input().split())
    andares.append((x, y))

andares.sort(key=lambda par: -(par[1]- par[0]))
consumido_ate_agora = 0
resposta=0

for x, y in andares:
    necessario=y+consumido_ate_agora
    resposta=max(resposta, necessario)
    consumido_ate_agora += x

print(resposta)
