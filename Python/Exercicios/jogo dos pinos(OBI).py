#prova 2020 fase 2

#explicação:
#verifica para cada pino "o" se ele pode se mover para cada uma das 4 direções


tabuleiro = []

for i in range(7):
    linha = input()
    tabuleiro.append(list(linha))

movimentos = 0

# cima
for i in range(2, 7):
    for j in range(7):
        if tabuleiro[i][j] == "o":
            if tabuleiro[i-1][j] == "o" and tabuleiro[i-2][j] == ".":
                movimentos += 1

# baixo
for i in range(5):
    for j in range(7):
        if tabuleiro[i][j] == "o":
            if tabuleiro[i+1][j] == "o" and tabuleiro[i+2][j] == ".":
                movimentos += 1

# esquerda
for i in range(7):
    for j in range(2, 7):
        if tabuleiro[i][j] == "o":
            if tabuleiro[i][j-1] == "o" and tabuleiro[i][j-2] == ".":
                movimentos += 1

# direita
for i in range(7):
    for j in range(5):
        if tabuleiro[i][j] == "o":
            if tabuleiro[i][j+1] == "o" and tabuleiro[i][j+2] == ".":
                movimentos += 1

print(movimentos)