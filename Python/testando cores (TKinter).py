from tkinter import *

def aparecer():
    texto.config(text="Que cor legal")
    texto.grid(column=0, row=1)

janela = Tk()
janela.title("Cores")
janela.geometry("400x300")
janela.configure(bg="#222222")

botao = Button(
    janela,
    text="Clique aqui",
    bg="#ff4d4d",
    fg="#ffffff",
    activebackground="#ff1a1a",
    activeforeground="#ffff00",
    command=aparecer,

)

botao.grid(column=0, row=0)

texto = Label(
    janela,
    text="",
    bg="#222222",
    fg="white",
    padx=50,
    pady=50,
    font=(20)
)

janela.mainloop()
