import random
from tkinter import *

contador = 0

def mover_botao():
    global contador

    contador += 1
    label.config(text=f"Clicadas: {contador}")

    x = random.randint(0, 550)
    y = random.randint(0, 550)
    botao.place(x=x, y=y)


janela = Tk()
janela.title("Botão que foge + contador")
janela.geometry("600x600")

label = Label(janela, text="Clicadas: 0", font= ("Arial", 14))
label.pack()

botao = Button(janela, text="Clique em mim", command=mover_botao)
botao.place(x=random.randint(0, 550), y=random.randint(0, 550))

janela.mainloop()
