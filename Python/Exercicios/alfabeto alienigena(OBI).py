k, n = map(int, input().split())

alfabeto = input()
mensagem = input()

pode = True

for letra in mensagem:
    encontrada = False

    for a in alfabeto:
        if letra == a:
            encontrada = True

    if encontrada == False:
        pode = False

if pode:
    print("S")
else:
    print("N")
