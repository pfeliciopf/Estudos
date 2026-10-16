#prova 2023 fase 2 
N = int(input())
S = input()

i = 0
resultado = []

while i < N:
    cont = 1

    while i + cont < N and S[i] == S[i + cont]:
        cont += 1

    resultado.append(str(cont))
    resultado.append(S[i])

    i += cont

print(" ".join(resultado))