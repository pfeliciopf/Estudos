import random
from tkinter import *

def aleatorio():
    x = random.choice(["cara", "coroa"])
    resultado.config(text=x)

def limpar():
    resultado.config(text="Aguardando...")

janela = Tk()
janela.geometry("400x400")

texto_apresentacao = Label(janela, text="Cara ou coroa")
texto_apresentacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Gire a moeda", command=aleatorio)
botao.grid(column=0, row=1)

resultado = Label(janela, text="Aguardando...")
resultado.grid(column=0, row=2, pady=10)

botao_limpar = Button(janela, text="Limpar resultado", command=limpar)
botao_limpar.grid(column=0, row=3)

janela.mainloop()