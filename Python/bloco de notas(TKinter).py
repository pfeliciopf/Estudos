from tkinter import *

janela = Tk()
janela.title("Bloco de Notas")

texto = Text(janela)
texto.pack(expand=True, fill=BOTH)

janela.mainloop()
