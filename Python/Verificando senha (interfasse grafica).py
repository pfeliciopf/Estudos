from tkinter import *

def verificar():
    try:
        senha_digitada = int(entrada.get())
        if senha_digitada == 1234:
            texto_resultado.config(text="A senha está correta")
            parabens= Label(janela, text= "como vc descobriu nossa senha super secreta? vc so pode ser um genio.")
            parabens.grid(row=4, column=0, padx=0, pady=10)
        else:
            texto_resultado.config(text="A senha está errada")
    except ValueError:
        texto_resultado.config(text="Digite apenas números!")

janela = Tk()
janela.geometry("400x300")
janela.title ("SENHA")

introdução = Label(janela, text="vc consegue descobrir a sequencia númerica")
introdução.grid(column=0, row=0, padx=0, pady= 10)

entrada = Entry(janela)
entrada.grid(row=1, column=0, padx=0, pady= 10)

botão = Button(janela, text="Verificar senha se esta correta", command=verificar)
botão.grid(row=2, column=0, padx=0, pady= 10)

texto_resultado = Label(janela, text="")
texto_resultado.grid(row=3, column=0, padx=0, pady= 10)

janela.mainloop()
