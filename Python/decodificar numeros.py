def decodificacao():
    lista = {
        1: "A", 2: "B", 3: "C",
        19: "D", 20: "E", 4: "F",
        18: "G", 21: "H", 5: "I",
        17: "J", 22: "K", 6: "L",
        16: "M", 23: "N", 7: "O",
        15: "P", 24: "Q", 8: "R", 9: "S",
        14: "T", 25: "U", 26: "V",
        13: "W", 12: "X", 11: "Y", 10: "Z"
    }
    telefone = input().split()
    resultado = ""
    for i in telefone:
        if i.isdigit() and int(i) in lista:
            resultado += lista[int(i)]
        else:
            resultado += i
    print(resultado)

decodificacao()