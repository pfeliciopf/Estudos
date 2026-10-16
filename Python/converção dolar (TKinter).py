from tkinter import *

def convercao():
    valor_dolar = float(dolar.get())
    valor_reais = float(entrada_reais.get())

    c = valor_reais / valor_dolar

    resultado.config(text=f"Com essa quantidade de reais você tem {c:.2f} dólares")

janela = Tk()
janela.geometry("800x800")
janela.title("Conversão do dólar")

texto_apresentacao = Label(
    janela,
    text="Coloque no primeiro espaço a cotação do dólar, e no segundo quantos reais você tem."
)
texto_apresentacao.grid(column=0, row=0)

dolar = Entry(janela)
dolar.grid(column=0, row=1)

entrada_reais = Entry(janela)
entrada_reais.grid(column=0, row=2)

botao = Button(janela, text="Clique para calcular", command=convercao)
botao.grid(column=0, row=3)

resultado = Label(janela, text="")
resultado.grid(column=0, row=4)

janela.mainloop()