caracteres1 = int(input())
palavra1 = input()

caracteres2 = int(input())
palavra2 = input()

contador = 0

for i in range(min(caracteres1, caracteres2)):
    if palavra1[i] == palavra2[i]:
        contador += 1
    else:
        break

print(contador)