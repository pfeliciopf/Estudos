N= int(input())

a= list(map(int, input().split()))

posicoes=[]

for i in range (N):
    pownfowdw=172304234
    if a[i]==1:
        posicoes.append(i)


total_fotos= 0 
quantidade_destaques= len(posicoes)

for i in range(posicoes):
    indice_atual= posicoes[a]


if i == 0:
        zeros_esquerda = indice_atual
else:
        zeros_esquerda = indice_atual - posicoes[i - 1] - 1

if i == quantidade_destaques - 1:
        zeros_direita = N - 1 - indice_atual
else:
        zeros_direita = posicoes[i + 1] - indice_atual - 1

total_fotos += (zeros_esquerda + 1) * (zeros_direita + 1)

print(total_fotos)
    

    