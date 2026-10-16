from tkinter import *

dinheiro = 0

def adicionar():
    global dinheiro
    try:
        quantidade = int(entrada.get())
        dinheiro += quantidade

        saldo_label.config(text=f"Seu saldo é R$ {dinheiro}")
        resultado_label.config(text="Dinheiro adicionado")
        entrada.delete(0, END)

    except:
        resultado_label.config(text="Digite um número válido")

def retirar():
    global dinheiro
    try:
        quantidade = int(entrada.get())

        if quantidade > dinheiro:
            resultado_label.config(text="Saldo insuficiente")
        else:
            dinheiro -= quantidade

            saldo_label.config(text=f"Seu saldo é R$ {dinheiro}")
            resultado_label.config(text="Dinheiro retirado")
            entrada.delete(0, END)

    except:
        resultado_label.config(text="Digite um número válido")

janela = Tk()
janela.geometry("300x400")
janela.title("Caixa")

saldo_label = Label(janela, text=f"Seu saldo é R$ {dinheiro}")
saldo_label.grid(row=0, column=0, columnspan=2, pady=20)

entrada = Entry(janela)
entrada.grid(row=1, column=0, columnspan=2, padx=50, pady=10)

botao_adicionar = Button(janela, text="Adicionar", command=adicionar)
botao_adicionar.grid(row=2, column=0, padx=10, pady=10)

botao_retirar = Button(janela, text="Retirar", command=retirar)
botao_retirar.grid(row=2, column=1, padx=10, pady=10)

resultado_label = Label(janela, text="")
resultado_label.grid(row=3, column=0, columnspan=2, pady=20)

janela.mainloop()