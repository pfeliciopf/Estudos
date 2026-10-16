centimetros=int(input())

pecas=1

while centimetros>=2:
    pecas*=4
    centimetros//=2

print(pecas)