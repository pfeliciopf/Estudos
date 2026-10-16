# 1. Lê a quantidade de estudantes (E), de pares "querem" (M) e "não querem" (D)
linha1 = input().split()
E = int(linha1[0])
M = int(linha1[1])
D = int(linha1[2])

# 2. Salva a lista de pares que gostariam de estar juntos
pares_querem = []
for _ in range(M):
    par = input().split()
    x = int(par[0])
    y = int(par[1])
    pares_querem.append([x, y])

# 3. Salva a lista de pares que NÃO gostariam de estar juntos
pares_nao_querem = []
for _ in range(D):
    par = input().split()
    u = int(par[0])
    v = int(par[1])
    pares_nao_querem.append([u, v])

# 4. Salva a divisão dos grupos feitos pela professora
grupos = []
total_grupos = E // 3
for _ in range(total_grupos):
    grupo = input().split()
    i = int(grupo[0])
    j = int(grupo[1])
    k = int(grupo[2])
    grupos.append([i, j, k])

# 5. Conta as violações
violacoes = 0

# Verifica se quem QUERIA ficar junto acabou separado
for x, y in pares_querem:
    juntos = False
    for g in grupos:
        if (x in g) and (y in g):  # Se os dois estão no mesmo grupo g
            juntos = True
    
    if juntos == False:  # Se não foram encontrados juntos em nenhum grupo
        violacoes += 1

# Verifica se quem NÃO QUERIA ficar junto acabou no mesmo grupo
for u, v in pares_nao_querem:
    juntos = False
    for g in grupos:
        if (u in g) and (v in g):  # Se os dois estão no mesmo grupo g
            juntos = True
            
    if juntos == True:  # Se foram encontrados juntos, é uma violação
        violacoes += 1

# 6. Mostra o resultado final
print(violacoes)
