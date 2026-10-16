pal = input("Digite uma palavra: ").lower()
vogais = "aeiou"
cons = "bcdfghjklmnpqrstvwxyz"

v_contador = 0
c_contador = 0

for letra in pal:
    if letra in vogais:
        v_contador += 1
    elif letra in cons:
        c_contador += 1

print(f"A palavra digitada tem {v_contador} vogais")
print(f"A palavra digitada tem {c_contador} consoantes")

if c_contador == 0 and v_contador == 0:
    print("Provavelmente essa palavra não existe, ou é uma onomatopeia (ou apenas símbolos).")

