#prova obi 2025 nivel junior fase 2

n = int(input())
tipos = list(map(int, input().split()))
precos = list(map(int, input().split()))
c = int(input())
clientes = list(map(int, input().split()))

objetos = []
for i in range(n):
    objetos.append([precos[i], tipos[i]])


objetos.sort()

total_arrecadado = 0

for u in clientes:
    if u == 0:
        if len(objetos) > 0:
            comprado = objetos.pop(0)
            total_arrecadado += comprado[0]
            
    else:  
        for obj in objetos:
            if obj[1] == u:
                total_arrecadado += obj[0]
                objetos.remove(obj)  
                break 

print(total_arrecadado)
