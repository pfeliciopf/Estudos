# 1. Definir a posição inicial (centro da grade 3x3)
x, y = 1, 1

# 2. Ler a sequência de comandos (ex: w a s d)
comandos = input("Digite os comandos separados por espaço: ").split()

# 3. Processar cada comando e aplicar os limites da grade [0, 2]
for comando in comandos:
    if comando == 'w':    # Sobe (diminui linha)
        y = max(0, y - 1)
    elif comando == 's':  # Desce (aumenta linha)
        y = min(2, y + 1)
    elif comando == 'a':  # Esquerda (diminui coluna)
        x = max(0, x - 1)
    elif comando == 'd':  # Direita (aumenta coluna)
        x = min(2, x + 1)

# 4. Exibir o resultado
posicao_final = [x, y]
print(f"Posição final: {posicao_final}")