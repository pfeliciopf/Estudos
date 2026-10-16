# Programa para calcular a tabuada usando while

numero = int(input("Digite um número: "))

contador = 1

print(f"\nTabuada do {numero}:\n")

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1