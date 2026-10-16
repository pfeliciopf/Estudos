def decodificacao():

    lista = {
        "A": 1, "B": 2, "C": 3,
        "D": 19, "E": 20, "F": 4,
        "G": 18, "H": 21, "I": 5,
        "J": 17, "K": 22, "L": 6,
        "M": 16, "N": 23, "O": 7,
        "P": 15, "Q": 24, "R": 8, "S": 9,
        "T": 14, "U": 25, "V": 26,
        "W": 13, "X": 12, "Y": 11, "Z": 10
    }

    telefone = input().upper()
    resultado = ""

    for i in telefone:
        if i in lista:
            resultado += str(lista[i])
        elif i.isdigit():
            resultado += i 
        else:
            resultado += i 

    print(int(resultado))

decodificacao()