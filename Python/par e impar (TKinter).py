from tkinter import *

# impar e par com interface
def verificacao():
    try:
        numero = int(entrada.get())
        if numero % 2 == 0:
            texto_resultado.config(text="o número digitado é par")
        else:
            texto_resultado.config(text="o número digitado é impar")
    except ValueError:
        texto_resultado.config(text="Digite apenas números!")

janela = Tk()
janela.geometry("400x200")
janela.title("Vidente dos números")

apresentacao = Label(janela, text="Olá bom dia\nPosso descobrir se qualquer número digitado é par ou impar")
apresentacao.grid(column=0, row=0)

entrada = Entry(janela)
entrada.grid(column=0, row=1)

botao_verificação = Button(janela, text="veja o futuro do seu amado número", command=verificacao)
botao_verificação.grid(column=0, row=2)

texto_resultado = Label(janela, text="")
texto_resultado.grid(column=0, row=3)

texto_finalizacao= Label(janela, text= "o que achou desse codigo?\nAvalie no nosso site site.com.br.\nMUITO OBG<3")
texto_finalizacao.grid(column= 0, row = 4)

janela.mainloop()

