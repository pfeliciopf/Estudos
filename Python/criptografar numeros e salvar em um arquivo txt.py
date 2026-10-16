def codificacao():
    lista = {
        "A": 1, "B": 2, "C": 3,
        "D": 19, "E": 20, "F": 4,
        "G": 18, "H": 21, "I": 5,
        "J": 17, "K": 22, "L": 6,
        "M": 16, "N": 23, "O": 7,
        "P": 15, "Q": 24, "R": 8,
        "S": 9, "T": 14, "U": 25,
        "V": 26, "W": 13, "X": 12,
        "Y": 11, "Z": 10
    }

    nome = input("Digite um nome: ").upper()

    resultado = ""

    for letra in nome:
        if letra in lista:
            resultado = resultado + str(lista[letra]) + " "

    print("Código:", resultado)

    arquivo = open("usuario.txt", "a")
    arquivo.write(nome + " = " + resultado + "\n")
    arquivo.close()


while True:
    codificacao()

    sair = input("Sair? (s/n): ")

    if sair == "s":
        break