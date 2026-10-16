from tkinter import *
import random


def troca_de_cor():
    rgb = ["red", "blue", "green"]
    escolha = random.choice(rgb)
    janela.config(bg=escolha)


janela = Tk()
janela.geometry("250x100")

texto = Label(janela, text="Aperte o botao e veja uma cor nova")
texto.grid(row=0, column=0, padx=20, pady=20)

botao = Button(janela, text="Mudar Cor", command=troca_de_cor)
botao.grid(row=1, column=0, padx=20, pady=10)

janela.mainloop()
