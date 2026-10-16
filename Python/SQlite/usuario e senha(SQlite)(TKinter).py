from tkinter import *
import sqlite3

# Conexão com o banco
conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    senha TEXT
)
""")
conexao.commit()

# Função para salvar
def salvar_usuario():
    nome = entrada_nome.get()
    senha = entrada_senha.get()

    if nome == "" or senha == "":
        resultado.config(text="Preencha todos os campos!")
        return

    cursor.execute(
        "INSERT INTO usuarios (nome, senha) VALUES (?, ?)",
        (nome, senha)
    )
    conexao.commit()

    resultado.config(text="Usuário cadastrado com sucesso!")

    entrada_nome.delete(0, END)
    entrada_senha.delete(0, END)

# Janela
janela = Tk()
janela.title("Cadastro de Usuário")
janela.geometry("350x180")

# Nome
Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entrada_nome = Entry(janela, width=25)
entrada_nome.grid(row=0, column=1, padx=10, pady=10)

# Senha
Label(janela, text="Senha:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entrada_senha = Entry(janela, width=25, show="*")
entrada_senha.grid(row=1, column=1, padx=10, pady=10)

# Botão
Button(janela, text="Salvar", command=salvar_usuario).grid(
    row=2, column=0, columnspan=2, pady=10
)

# Mensagem
resultado = Label(janela, text="")
resultado.grid(row=3, column=0, columnspan=2)

janela.mainloop()

conexao.close()