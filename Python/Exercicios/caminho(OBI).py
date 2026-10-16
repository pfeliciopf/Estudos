#prova obi nivel junior 2022 fase 2

#Lê a quantidade de postes e as potências das lâmpadas
N = int(input())
potencias = []

for _ in range(N):
    potencias.append(int(input()))

#Identifica quais trechos são escuros (1) e quais são claros (0)
trechos = []
for i in range(N):
    vizinho = (i + 1) % N  # O resto da divisão (%) faz o último poste ligar de volta ao primeiro
    if potencias[i] + potencias[vizinho] < 1000:
        trechos.append(1)  # 1 significa trecho escuro
    else:
        trechos.append(0)  # 0 significa trecho claro

trechos_circulares = trechos + trechos

#Conta a maior sequência de trechos escuros (1s) seguidos
maior_sequencia = 0
sequencia_atual = 0

for t in trechos_circulares:
    if t == 1:
        sequencia_atual += 1
        if sequencia_atual > maior_sequencia:
            maior_sequencia = sequencia_atual
    else:
        sequencia_atual = 0  # Se achou um trecho claro, zera a contagem atual

#Garante que o resultado não seja maior que o tamanho total da pista
if maior_sequencia > N:
    maior_sequencia = N

print(maior_sequencia)

