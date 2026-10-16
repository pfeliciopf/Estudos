import time
import random

acertos = 0
tempos = []

print("Prepare-se...")

for i in range(10):
    print(f"\nRodada {i+1}")
    time.sleep(1)

    letra = random.choice("abcdefghijklmnopqrstuvwxyz")
    print("Digite esta letra:", letra)

    inicio = time.time()
    resposta = input(">> ")
    fim = time.time()

    tempo = fim - inicio
    tempos.append(tempo)

    if resposta == letra and tempo <= 3:
        print("Acertou rápido ")
        acertos += 1
    else:
        print("Errou ou foi lento")

print("\n=== RESULTADO FINAL ===")
print("Acertos:", acertos)

media = sum(tempos) / len(tempos)
print("Tempo médio:", round(media, 2), "segundos")
print ("o tempo final foi", tempo, "volte sempre")

tempos.sort()
print("Melhor tempo:", tempos[0])

tempos.sort()
print("Pior tempo:", tempos[0])
