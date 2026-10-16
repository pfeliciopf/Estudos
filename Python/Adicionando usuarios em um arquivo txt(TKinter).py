import tkinter as tk

def salvar_nome():
    nome = entrada.get()

    arquivo = open("usuario.txt", "a")
    arquivo.write(nome + "\n")
    arquivo.close()

    resultado.config(text="Nome adicionado com sucesso!")
    entrada.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de Usuário")

tk.Label(janela, text="Digite seu nome:").pack()

entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Salvar", command=salvar_nome).pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()