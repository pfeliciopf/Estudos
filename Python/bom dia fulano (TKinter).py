from tkinter import *

def nome_digitado():
    nome = entrada.get()
    mensagem_legal.config(text=f"bom dia {nome}")

janela = Tk()
janela.geometry("200x200")
janela.title("bom dia amigo")

introducao= Label(janela, text= "Bom dia, qual o seu nome?")
introducao.grid(column = 0, row= 0)

entrada = Entry(janela)
entrada.grid(row=1, column=0, padx=0, pady=10)

botão = Button(janela, text="Receber mensagem legal", command=nome_digitado)
botão.grid(row=2, column=0, padx=0, pady=10)

mensagem_legal = Label(janela, text="")
mensagem_legal.grid(column=0, row=3, padx=10, pady=10)

janela.mainloop()
