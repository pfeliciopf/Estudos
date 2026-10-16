#prova 2024 fase 2 turno b

#explicação:
# é necessario que os tres palitos obedeção 3 condoções para que se forme um triangulo
# a + b > c
# a + c > b
# b + c > a

n = int(input())
palitos = list(map(int, input().split()))

resposta = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):

            a = palitos[i]
            b = palitos[j]
            c = palitos[k]

            if a + b > c and a + c > b and b + c > a:
                resposta += 1

print(resposta)
