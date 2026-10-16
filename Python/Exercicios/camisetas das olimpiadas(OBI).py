N = int(input())
T = list(map(int, input().split()))
P = int(input())
M = int(input())

peq = T.count(1)
med = T.count(2)

if peq <= P and med <= M:
    print("S")
else:
    print("N")