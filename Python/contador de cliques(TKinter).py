import tkinter as tk

cliques = 0

def contar():
    global cliques
    cliques += 1
    label.config(text=f"Cliques: {cliques}")

janela = tk.Tk()
janela.title("Contador de Cliques")

label = tk.Label(janela, text="Cliques: 0")
label.pack(pady=10)

botao = tk.Button(janela, text="Clique aqui", command=contar)
botao.pack()

janela.mainloop()