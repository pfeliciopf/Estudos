#2021 fase 3

n = int(input())

if n <= 5:
    mao_esq = "I" * n if n > 0 else "*"
    mao_dir = "*"
else:
    mao_esq = "IIIII"
    mao_dir = "I" * (n - 5)

print(mao_esq)
print(mao_dir)
