from tkinter import *
from deep_translator import GoogleTranslator

#pip install --break-system-packages deep-translator

def traduzir():
    texto = entrada.get()

    traducao = GoogleTranslator(source="en", target="pt").translate(texto)

    resultado.config(text=traducao)

janela = Tk()
janela.title("Tradutor")
janela.geometry("400x400")

Label(janela, text="Texto em inglês:").grid(row=0, column=0)

entrada = Entry(janela, width=30)
entrada.grid(row=0, column=1)

Button(janela, text="Traduzir", command=traduzir).grid(row=1, column=0, columnspan=2)

resultado = Label(janela, text="")
resultado.grid(row=2, column=0, columnspan=2)

janela.mainloop()