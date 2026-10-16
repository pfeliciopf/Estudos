#prova 2023- nivel junior- f1
N = int(input())
R = int(input())
P = int(input())

total = N
novas = N
dias = 0

while total < P:
    novas = novas * R
    total += novas
    dias += 1

print(dias)