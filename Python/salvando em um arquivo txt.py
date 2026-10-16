while True:
    nome = input("Digite seu nome: ")

    arquivo = open("usuario.txt", "a")

    arquivo.write(nome + "\n")

    arquivo.close()

    print("Nome adicionado com sucesso!")