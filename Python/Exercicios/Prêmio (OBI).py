#prova 2023- nivel junior- f1
p = int(input())
d = int(input())
b = int(input())

soma = p * 1 + d * 2 + b * 3

if soma >= 150:
    print("B")
elif soma >= 120:
    print("D")
elif soma >= 100:
    print("P")
else:
    print("N")