import tkinter as tk
import random

opcoes = ["Pedra", "Papel", "Tesoura"]

def jogar(escolha):
    computador = random.choice(opcoes)

    if escolha == computador:
        texto = "Empate!"
    elif (
        (escolha == "Pedra" and computador == "Tesoura") or
        (escolha == "Papel" and computador == "Pedra") or
        (escolha == "Tesoura" and computador == "Papel")
    ):
        texto = "Você venceu!"
    else:
        texto = "Você perdeu!"

    resultado.config(
        text=f"Computador: {computador}\n{texto}"
    )

janela = tk.Tk()
janela.title("Pedra, Papel ou Tesoura")

for opcao in opcoes:
    tk.Button(
        janela,
        text=opcao,
        command=lambda o=opcao: jogar(o)
    ).pack(pady=2)

resultado = tk.Label(janela, text="")
resultado.pack(pady=10)

janela.mainloop()