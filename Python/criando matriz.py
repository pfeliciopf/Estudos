# Cria a matriz vazia
turma = []

# Cria 5 linhas
for i in range(5):

    # Cria uma linha vazia
    linha = []

    # Adiciona 5 valores na linha
    for j in range(5):
        # Lê uma nota e transforma em inteiro
        nota = int(input(f"Digite a nota [{i},{j}]: "))

        # Coloca a nota na linha
        linha.append(nota)

    # Coloca a linha pronta na matriz
    turma.append(linha)


# Percorre a matriz e imprime cada elemento
for i in range(5):
    for j in range(5):

        # Acessa o valor da linha i e coluna j
        print(turma[i][j])
