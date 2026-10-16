import tkinter as tk
import random

numero = random.randint(1, 20)

def verificar():
    chute = int(entrada.get())

    if chute < numero:
        resultado.config(text="Muito baixo!")
    elif chute > numero:
        resultado.config(text="Muito alto!")
    else:
        resultado.config(text="Acertou!")

janela = tk.Tk()
janela.title("Adivinhe o Número")

tk.Label(janela, text="Digite um número de 1 a 20").pack()

entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Verificar", command=verificar).pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()