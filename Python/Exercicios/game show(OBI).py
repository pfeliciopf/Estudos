#prova obi 2024 fase 2 turno B

#verifica as letras, se for "e" o programa multiplica a sala *2
#se for "d" a sal *2+1

sala = 1

n = int(input())
instrucoes = input()

for letra in instrucoes:
    if letra == "E":
        sala = sala * 2
    else:
        sala = sala * 2 + 1

print(sala)
