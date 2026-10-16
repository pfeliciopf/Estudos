import tkinter as tk
import random

def gerar():
    numero = random.randint(1, 100)
    resultado.config(text=f"Número: {numero}")

janela = tk.Tk()
janela.title("Número Aleatório")

tk.Button(janela, text="Gerar", command=gerar).pack(pady=10)

resultado = tk.Label(janela, text="Clique no botão")
resultado.pack()

janela.mainloop()