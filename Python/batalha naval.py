import random

# Cria uma matriz 4x4
tabuleiro = [["~~" for _ in range(4)] for _ in range(4)]
1
# Sorteia a posição do navio
navio_linha = random.randint(0, 3)
navio_coluna = random.randint(0, 3)

tentativas = 5

while tentativas > 0:
    # Mostra o tabuleiro
    print("\n  0 1 2 3")
    for i in range(4):
        print(i, end=" ")
        print(" ".join(tabuleiro[i]))

    print(f"\nTentativas restantes: {tentativas}")

    # Entrada do jogador
    linha = int(input("Digite a linha: "))
    coluna = int(input("Digite a coluna: "))

    # Código gabarito
    if linha == 123456789 and coluna == 987654321:
        print("\n!CÓDIGO CERTO!")
        print(f"O navio está na linha {navio_linha}")
        print(f"O navio está na coluna {navio_coluna}")

        continuar = input("Quer continuar jogando? (sim/nao): ").lower()

        if continuar == "sim":
            continue
        elif continuar == "nao":
            break
        else:
            print("Resposta inválida!")
            continue

    # Verifica se a posição é válida
    if linha < 0 or linha > 3 or coluna < 0 or coluna > 3:
        print("Posição inválida!")
        continue

    # Verifica se já tentou essa posição
    if tabuleiro[linha][coluna] == "X":
        print("Você já tentou essa posição!")
        continue

    # Acertou o navio
    if linha == navio_linha and coluna == navio_coluna:
        tabuleiro[linha][coluna] = "N"

        print("\n  0 1 2 3")
        for i in range(4):
            print(i, end=" ")
            print(" ".join(tabuleiro[i]))

        print("\nParabéns! Você afundou o navio!")
        break

    # Errou
    tabuleiro[linha][coluna] = "X"
    print("Água!")
    tentativas -= 1

else:
    print("\nFim de jogo! Você perdeu.")
    print(f"O navio estava na posição ({navio_linha}, {navio_coluna}).")