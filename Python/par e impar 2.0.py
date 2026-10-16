from tkinter import *

# impar e par com interface
def ip():
    try:
        numero = int(entrada.get())
        if numero % 2 == 0:
            texto_resultado.config(text="o número digitado é par")
        else:
            texto_resultado.config(text="o número digitado é impar")
    except ValueError:
        texto_resultado.config(text="Digite apenas números!")

janela = Tk()
janela.geometry("400x100")
janela.title("Vidente dos números")

apresentacao = Label(janela, text="Olá bom dia, posso descobrir se qualquer número digitado é par ou impar")
apresentacao.grid(column=0, row=0)

entrada = Entry(janela)
entrada.grid(column=0, row=1)

botao_verificação = Button(janela, text="veja o futuro do seu amado número", command=ip)
botao_verificação.grid(column=0, row=2)

texto_resultado = Label(janela, text="")
texto_resultado.grid(column=0, row=3)

janela.mainloop()
