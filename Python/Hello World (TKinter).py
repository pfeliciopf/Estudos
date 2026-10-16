from tkinter import *

def hello():
    mensagem_legal.config(text="OI AMIGO")
    print("OI AMIGO")

def mostrar_pergunta():
    texto2 = Label(janela, text="Já clicou?")
    texto2.grid(column=0, row=4, padx=10, pady=10)

janela = Tk()
janela.geometry("300x300")
janela.title("Hello")

texto = Label(janela, text="clique no botão para ver uma incrivel mensagem")
texto.grid(column=0, row=0, padx=10, pady=10)

mensagem_legal = Label(janela, text="")
mensagem_legal.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text="clica ai mano", command=hello)
botao.grid(column=0, row=2, padx=10, pady=10)

janela.after(5000, mostrar_pergunta)

janela.mainloop()
