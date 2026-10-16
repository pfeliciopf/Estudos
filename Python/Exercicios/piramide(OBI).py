#prova obi nivel junior 2022 fase 2

tamanho=int(input())

for i in range(tamanho):
    linha=[]
    for j in range(tamanho):
        distancia_cima=i
        distancia_esquerda=j
        distancia_baixo=tamanho-i-1
        distancia_direita= tamanho-j-1

        menor_distancia=min(distancia_cima, distancia_baixo, distancia_direita, distancia_esquerda)
        valor_celula=menor_distancia+1

        linha.append(valor_celula)

    print(*linha)
