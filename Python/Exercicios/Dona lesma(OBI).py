#prova 2020 fase 2

altura = int(input())
distancia = int(input())
escorrega = int(input())

subiu = 0
dias = 0

while subiu < altura:
    dias += 1
    subiu += distancia

    if subiu >= altura:
        break

    subiu -= escorrega

print(dias)