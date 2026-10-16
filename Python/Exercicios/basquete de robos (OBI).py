distancia_lanc = int(input())

if distancia_lanc <= 2000 and distancia_lanc > 1400:
    print(3)
elif distancia_lanc <= 1400 and distancia_lanc > 800:
    print(2)
else:
    print(1)