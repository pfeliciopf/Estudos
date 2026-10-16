dicionario={
    #nome e idade em um dicionario
    "ZÉZINHO": 15,
    "LUIZINHO": 10

}

print(dicionario)
pergunta= str(input("de qual pessoa vc gostaria de ver?:  ")).upper()

print("A idade dele é:")
print(dicionario[pergunta])