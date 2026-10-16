print("=== SISTEMA MASTER PRO ===")

while True:
    r = int(input("Escolha uma função:\n1 - Calculadora\n2 - Jogo de palavras\n3 - Sair\n"))

    if r == 3:
        break

    elif r == 1:
        y = input("Escolha: 1-soma, 2-divisão, 3-multiplicação\n")

        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if y == "1":
            print(a + b)
        elif y == "2":
            if b != 0:
                print(a / b)
            else:
                print("erro")
        elif y == "3":
            print(a * b)

    elif r == 2:
        import time
        import random

        x = "abcdefghijklmnopqrstuvwxyz"
        melhor = 1000
        pior = 0
        soma = 0
        acertos = 0

        vezes = int(input("Quantas vezes quer jogar? "))

        time.sleep(1)

        for i in range(vezes):
            y = random.choice(x)
            print(y)

            inicio = time.time()
            entrada = input()
            final = time.time()

            tempo = final - inicio

            if entrada.lower() == y:
                acertos += 1
                soma += tempo

                if tempo < melhor:
                    melhor = tempo
                if tempo > pior:
                    pior = tempo

        if acertos > 0:
            print(round(melhor, 2))
            print(round(pior, 2))
            print(round(soma / acertos, 2))
