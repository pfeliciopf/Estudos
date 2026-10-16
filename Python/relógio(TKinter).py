import time
import tkinter as tk

janela = tk.Tk()
janela.title("Relógio")

texto = tk.Label(janela, font=("Arial", 40))
texto.pack()

def atualizar():
    hora = time.strftime("%H:%M:%S")
    texto.config(text=hora)
    janela.after(1000, atualizar)

atualizar()

janela.mainloop()