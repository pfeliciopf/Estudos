import tkinter as tk
import random

cores = ["red", "blue", "green", "yellow", "purple", "orange"]

def mudar_cor():
    janela.config(bg=random.choice(cores))

janela = tk.Tk()
janela.title("Troca de Cor")
janela.geometry("300x200")

tk.Button(janela, text="Mudar Cor", command=mudar_cor).pack(pady=50)

janela.mainloop()