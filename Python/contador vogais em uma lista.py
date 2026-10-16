lista_frutas=[
    "banana",
    "maçã",
    "uva",
    "laranja",
    "pera",
    "melão"
]

vogais=["a","e","i","o","u"]

contador_vogais=0
contador_consoantes=0

for fruta in lista_frutas:
    for letra in fruta:
        if letra in vogais:
            contador_vogais+=1

        else:
            contador_consoantes+=1

print(f"vogais: {contador_vogais}")
print(f"consoantes: {contador_consoantes}")

