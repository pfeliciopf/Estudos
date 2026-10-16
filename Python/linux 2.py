# LINUX 2
import time
def tabuada():
    multiplicador= int(input("qual sera o multiplicador?: "))
    num = int(input("qual sera o número a ser multiplcado?: "))
    c = 1
    while c <= (multiplicador):
        print(num, "x", c, "=", num * c)
        c += 1


def calculadora():
    print("Calculadora:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Tabuada")
    print("4 - Divisão")

    escolha = int(input("Qual conta você gostaria de realizar? "))

    if escolha == 1:
        quantidade = int(input("Quantos números deseja somar? "))
        resultado = 0

        for i in range(quantidade):
            numero = int(input("Digite um número: "))
            resultado += numero

        print("Resultado:", resultado)

    elif escolha == 2:
        quantidade = int(input("Quantos números deseja subtrair? "))
        resultado = int(input("Digite o primeiro número: "))

        for i in range(quantidade - 1):
            numero = int(input("Digite outro número: "))
            resultado -= numero

        print("Resultado:", resultado)

    elif escolha == 3:
        quantidade = int(input("Quantos números deseja multiplicar? "))
        resultado = 1

        for i in range(quantidade):
            numero = int(input("Digite um número: "))
            resultado *= numero

        print("Resultado:", resultado)

    elif escolha == 5:
        divisao1= int(input("escolha o divisor: "))
        divisao2= int(input("escolha o número que sera dividido")) 

        divisão_total= (divisao2)/divisao1

        print(f"O resultado da divisão foi: {divisão_total}")

    elif escolha == 4:
        tabuada()


def timer():
    segundos = int(input("Digite o tempo em segundos: "))

    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)

    print("Tempo acabou!")


def conversao():
    print("Conversão:")
    print("1 - Metros para centímetros")

    escolha = int(input("Escolha: "))

    if escolha == 1:
        metros = float(input("Digite o valor em metros: "))
        print("Resultado:", metros * 100, "cm")


# LOOP PRINCIPAL
while True:
    inicio = input("Você gostaria de entrar/continuar no sistema Linux 2? sim/nao: ").lower()

    if inicio == "nao":
        print("Saindo...")
        break

    print("Escolha uma função:")
    print("1 - Calculadora")
    print("2 - Timer")
    print("3 - Conversão")
    print("4 - Tabuada")

    escolha = int(input("Digite: "))

    if escolha == 1:
        calculadora()
    elif escolha == 2:
        timer()
    elif escolha == 3:
        conversao()
    elif escolha == 4:
        tabuada()