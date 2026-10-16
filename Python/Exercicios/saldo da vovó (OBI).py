#prova 2008

n, saldo = map(int, input().split())

menor = saldo

for _ in range(n):
    movimento = int(input())
    saldo += movimento

    if saldo < menor:
        menor = saldo

print(menor)