#gerador de senhas arcaico
import random

caracteres = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*?")

while True:
    senha = ""

    # Pega 8 caracteres aleatórios
    for i in range(8):
        senha = senha + random.choice(caracteres)

    maiuscula = False
    minuscula = False
    numero = False
    especial = False

    # Verifica cada caractere
    for letra in senha:
        if letra >= "A" and letra <= "Z":
            maiuscula = True
        elif letra >= "a" and letra <= "z":
            minuscula = True
        elif letra >= "0" and letra <= "9":
            numero = True
        else:
            especial = True

    if maiuscula == True and minuscula == True and numero == True and especial == True:
        print("Senha:", senha)
        print("Maiúscula:", maiuscula)
        print("Minúscula:", minuscula)
        print("Número:", numero)
        print("Especial:", especial)
        break
