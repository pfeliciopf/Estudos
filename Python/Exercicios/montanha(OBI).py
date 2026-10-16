a = int(input())
n = list(map(int, input().split()))

resultado = "N"

for i in range(1, a - 1):
    if n[i - 1] > n[i] and n[i] < n[i + 1]:
        resultado = "S"

print(resultado)
