#prova obi n junior fase 2 prova 2015

N = int(input())
matriz = []
soma_linhas = [0] * N
soma_colunas = [0] * N

# Lê a matriz e calcula as somas das linhas e colunas
for i in range(N):
  linha = list(map(int, input().split()))
  matriz.append(linha)
  for j in range(N):
    soma_linhas[i] += linha[j]
    soma_colunas[j] += linha[j]

# Encontra o peso máximo
peso_maximo = -1
for i in range(N):
  for j in range(N):
    peso_atual = soma_linhas[i] + soma_colunas[j] - 2 * matriz[i][j]
    if peso_atual > peso_maximo:
      peso_maximo = peso_atual

print(peso_maximo)
