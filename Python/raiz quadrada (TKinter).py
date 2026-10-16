import math
from tkinter import *

def calcular():
    try:
        r = math.sqrt(float(entrada.get()))
        resultado.config(text=f"Raiz: {r:.4f}")
    except ValueError:
        resultado.config(text="Digite um número válido!")

janela = Tk()
janela.title("Raiz Quadrada")
janela.geometry("400x400")

texto = Label(janela, text="Número:")
texto.grid(row=0, column=0, padx=10, pady=10)

entrada = Entry(janela, font=("Arial", 14))
entrada.grid(row=0, column=1, padx=10, pady=10)

botao = Button(janela, text="Calcular", command=calcular)
botao.grid(row=1, column=0, columnspan=2, pady=10)

resultado = Label(janela, text="", font=("Arial", 14))
resultado.grid(row=2, column=0, columnspan=2, pady=10)

janela.mainloop()
