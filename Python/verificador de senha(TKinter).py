from tkinter import *

def verificar():
    senha = entrada.get()
    pontuacao = 0

    if "_" in senha:
        pontuacao += 1

    if "." in senha:
        pontuacao += 1

    if "@" in senha:
        pontuacao += 1

    if any(c in "0123456789" for c in senha):
        pontuacao += 1

    if any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in senha):
        pontuacao += 1

    if any(c in "abcdefghijklmnopqrstuvwxyz" for c in senha):
        pontuacao += 1

    if pontuacao <= 2:
        resultado.config(text=f"Pontuação: {pontuacao}\nFoi ruim")
    elif pontuacao <= 3:
        resultado.config(text=f"Pontuação: {pontuacao}\nFoi mediano")
    elif pontuacao <= 4:
        resultado.config(text=f"Pontuação: {pontuacao}\nFoi bom")
    else:
        resultado.config(text=f"Pontuação: {pontuacao}\nPerfeito")

janela = Tk()
janela.geometry("400x200")
janela.title("Verificador de Senha")

Label(janela, text="Senha:").grid(row=0, column=0, padx=10, pady=10)

entrada = Entry(janela, width=30, show="*")
entrada.grid(row=0, column=1, padx=10, pady=10)

Button(janela, text="Verificar", command=verificar).grid(row=1, column=0, columnspan=2, pady=10)

resultado = Label(janela, text="")
resultado.grid(row=2, column=0, columnspan=2)

janela.mainloop()
