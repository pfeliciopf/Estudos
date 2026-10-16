import tkinter as tk
import sqlite3

conexao = sqlite3.connect("usuarios.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT
)
""")
conexao.commit()

def salvar_nome():
    nome = entrada.get()

    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    conexao.commit()

    resultado.config(text="Nome salvo com sucesso!")
    entrada.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de Usuário")
janela.geometry("400x400")

tk.Label(janela, text="Digite seu nome:").pack()

entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Salvar", command=salvar_nome).pack()

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()

conexao.close()