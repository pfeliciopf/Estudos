#prova 2025 fase 2

n, m = map(int, input().split())
necessario = 1 + (n - 1) * 5
if necessario <= m:
    print("S")
else:
    print("N")  