from tkinter import *
import os

def senha():
    caracteres = list("abcdefghijklmnopqrstuvwxyz1234567890_")
    s = entrada.get()

    for x in s:
        if x not in caracteres:
            texto.config(text="Senha inválida")
            return

    with open("senha.txt", "w") as arquivo:
        arquivo.write(s)

    home()

def home():
    limpar()

    Button(janela, text="Bloco de notas", command=bloco).grid(row=0, column=0)
    Button(janela, text="Timer", command=timer).grid(row=0, column=1)
    Button(janela, text="Senhas", command=senhas).grid(row=1, column=0)
    Button(janela, text="Boletim", command=boletim).grid(row=1, column=1)

def bloco():
    limpar()

    texto_bloco = Text(janela)
    texto_bloco.grid(row=0, column=0)

    def salvar():
        with open("notas.txt", "w") as arquivo:
            arquivo.write(texto_bloco.get("1.0", END))

    Button(janela, text="Salvar", command=salvar).grid(row=1, column=0)
    Button(janela, text="Voltar", command=home).grid(row=2, column=0)

def timer():
    limpar()

    tempo = Label(janela, text="0")
    tempo.grid(row=0, column=0)

    segundos = [0]

    def contar():
        segundos[0] += 1
        tempo.config(text=segundos[0])
        janela.after(1000, contar)

    Button(janela, text="Começar", command=contar).grid(row=1, column=0)
    Button(janela, text="Voltar", command=home).grid(row=2, column=0)

def senhas():
    limpar()

    site = Entry(janela)
    site.grid(row=0, column=1)

    senha = Entry(janela, show="*")
    senha.grid(row=1, column=1)

    def salvar():
        with open("senhas.txt", "a") as arquivo:
            arquivo.write(site.get() + " " + senha.get() + "\n")

    Label(janela, text="Site").grid(row=0, column=0)
    Label(janela, text="Senha").grid(row=1, column=0)

    Button(janela, text="Salvar", command=salvar).grid(row=2, column=0)
    Button(janela, text="Voltar", command=home).grid(row=2, column=1)

def boletim():
    limpar()

    notas = []

    for i in range(4):
        n = Entry(janela, width=5)
        n.grid(row=0, column=i)
        notas.append(n)

    resultado = Label(janela, text="")
    resultado.grid(row=2, column=0, columnspan=4)

    def calcular():
        try:
            media = sum(float(n.get()) for n in notas) / 4
            resultado.config(text=f"Média: {media:.2f}")
        except:
            resultado.config(text="Digite números")

    Button(janela, text="Calcular", command=calcular).grid(
        row=1, column=0, columnspan=4
    )

    Button(janela, text="Voltar", command=home).grid(
        row=3, column=0, columnspan=4
    )

def limpar():
    for x in janela.winfo_children():
        x.destroy()

janela = Tk()
janela.title("Meu Sistema")
janela.geometry("400x300")

texto = Label(janela, text="Digite a senha:")
texto.grid(row=0, column=0)

entrada = Entry(janela, show="*")
entrada.grid(row=1, column=0)

Button(janela, text="Entrar", command=senha).grid(row=1, column=1)

janela.mainloop()