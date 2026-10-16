lista = []

soma = 0

for i in range(5):
    numero = int(input())
    lista.append(numero)

for numero in lista:
    soma += numero

print(soma)