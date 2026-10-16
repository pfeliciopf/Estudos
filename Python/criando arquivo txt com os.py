import os

nome = "teste.txt"

if not os.path.exists(nome):

    with open(nome, "w") as arquivo:
        arquivo.write("Olá, mundo!")

    print("Arquivo criado!")

else:
    print("O arquivo já existe.")