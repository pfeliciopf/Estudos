import tkinter as tk

janela = tk.Tk()
janela.geometry("300x300")

x = 150
y = 150

personagem = tk.Label(janela, text="0")
personagem.place(x=x, y=y)

def mover(event):
    global x, y

    tecla = event.keysym.lower()

    if tecla == "w":
        y -= 10
    elif tecla == "s":
        y += 10
    elif tecla == "a":
        x -= 10
    elif tecla == "d":
        x += 10

    personagem.place(x=x, y=y)

janela.bind("<KeyPress>", mover)
janela.focus_set()

janela.mainloop()