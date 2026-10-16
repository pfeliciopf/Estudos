r, n= int(input())

menor_preco= {}

for i in range(n):
    tipo, preco=int(input()).split()

    if tipo not in menor_preco:
        menor_preco[tipo] = preco
    else:
        menor_preco[tipo] = min(menor_preco[tipo], preco)

precos = list(menor_preco.values())
precos.sort()

resposta = 0

for preco in precos:
    if R >= preco:
        R -= preco
        resposta += 1
    else:
        break

print(resposta)
