lista = []

numPlist = []
numIlist = []


# Criando a matriz 3x3
for i in range(3):
    linha = []

    for j in range(3):
        valor = int(input())
        linha.append(valor)

    lista.append(linha)


# Imprimindo a matriz como tabela
print("Matriz:")

for i in range(3):
    for j in range(3):
        print(lista[i][j], end=" ")

    print()


# Separando pares e ímpares
for i in range(3):
    for j in range(3):

        if lista[i][j] % 2 == 0:
            numPlist.append(lista[i][j])

        else:
            numIlist.append(lista[i][j])


print("Números pares:", numPlist)
print("Números ímpares:", numIlist)


# Verificando se existem pares ou ímpares
if len(numPlist) == 0:
    print("Não tem números pares")

if len(numIlist) == 0:
    print("Não tem números ímpares")