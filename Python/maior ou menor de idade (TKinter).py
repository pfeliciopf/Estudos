from tkinter import *

# impar e par com interface
def ip():
    try:
        numero = int(entrada.get())
        if numero >= 18 and numero < 60:
            texto_resultado.config(text="vc é maior de idade, viva seus sonhos")
        elif numero >= 60:
            texto_resultado.config(text= "vc pode pegar onibus de graça")
        elif numero <18 and numero >3:
            texto_resultado.config(text= "vc é menor de idade")
        else:
            texto_resultado.config (text= "vc provavelmente não sabe escrever.")
    except ValueError:
        texto_resultado.config(text="Digite apenas números!")

janela = Tk()
janela.geometry("207x200")
janela.title("Idade")

apresentacao = Label(janela, text="Quantos anos vc tem?")
apresentacao.grid(column=0, row=0)

entrada = Entry(janela)
entrada.grid(column=0, row=1)

botao_verificação = Button(janela, text="veja se vc é maior ou menor de idade", command=ip)
botao_verificação.grid(column=0, row=2)

texto_resultado = Label(janela, text="")
texto_resultado.grid(column=0, row=3)

janela.mainloop()
