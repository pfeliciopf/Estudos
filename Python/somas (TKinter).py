from tkinter import *

def soma():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())

    resultado = num1 + num2

    escrever_resultado.config(text=f"O resultado da sua soma foi: {resultado}")

janela = Tk()
janela.geometry("400x400")
janela.title("Soma")

texto1 = Label(janela, text="Escreva abaixo os dois números que você deseja somar.")
texto1.grid(column=0, row=0)

entrada1 = Entry(janela)
entrada1.grid(column=0, row=1)

entrada2 = Entry(janela)
entrada2.grid(column=0, row=2)

botao = Button(janela, text="Clique aqui para somar", command=soma)
botao.grid(column=0, row=3)

escrever_resultado = Label(janela, text="")
escrever_resultado.grid(column=0, row=4)

janela.mainloop()
