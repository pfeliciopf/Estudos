lista = []
entrada = map(int, input().split())
for num in entrada:
    if num %2==0:
        continue
    if num % 2 != 0:
        lista.append(num)
print("os números impares são: ->")
print(lista)
