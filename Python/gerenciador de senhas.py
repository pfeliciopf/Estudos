from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Gerenciador de Senhas")
janela.geometry("400x300")

# ---------------- CADASTRAR ----------------

Label(janela, text="O quê?").grid(row=0, column=0)

entrada_oque = Entry(janela)
entrada_oque.grid(row=0, column=1)

Label(janela, text="Usuário").grid(row=1, column=0)

entrada_usuario = Entry(janela)
entrada_usuario.grid(row=1, column=1)

Label(janela, text="Senha").grid(row=2, column=0)

entrada_senha = Entry(janela, show="*")
entrada_senha.grid(row=2, column=1)

# ---------------- ATUALIZAR LISTA ----------------

def atualizar_lista():

    lista = []

    try:

        arquivo = open("senhas.txt", "r", encoding="utf-8")

        for linha in arquivo:

            dados = linha.strip().split("|")

            if dados[0] not in lista:
                lista.append(dados[0])

        arquivo.close()

    except:
        pass

    caixa["values"] = lista

    if len(lista) > 0:
        caixa.current(0)

# ---------------- SALVAR ----------------

def salvar():

    arquivo = open("senhas.txt", "a", encoding="utf-8")

    arquivo.write(
        entrada_oque.get() + "|" +
        entrada_usuario.get() + "|" +
        entrada_senha.get() + "\n"
    )

    arquivo.close()

    entrada_oque.delete(0, END)
    entrada_usuario.delete(0, END)
    entrada_senha.delete(0, END)

    atualizar_lista()

    resultado.config(text="Cadastro salvo!")

Button(janela, text="Salvar", command=salvar).grid(row=3, column=0, columnspan=2)

# ---------------- MOSTRAR ----------------

Label(janela, text="Mostrar o quê?").grid(row=4, column=0)

caixa = ttk.Combobox(janela, state="readonly")
caixa.grid(row=4, column=1)

def mostrar():

    try:

        arquivo = open("senhas salvas.txt", "r", encoding="utf-8")

        for linha in arquivo:

            dados = linha.strip().split("|")

            if dados[0] == caixa.get():

                resultado.config(
                    text="Usuário: " + dados[1] +
                    "\nSenha: " + dados[2]
                )

                arquivo.close()
                return

        resultado.config(text="Cadastro não encontrado.")

        arquivo.close()

    except:

        resultado.config(text="Nenhum cadastro.")

# ---------------- RETIRAR ----------------

def retirar():

    try:

        arquivo = open("senhas.txt", "r", encoding="utf-8")

        linhas = arquivo.readlines()

        arquivo.close()

        for i in range(len(linhas)):

            dados = linhas[i].strip().split("|")

            if dados[0] == caixa.get():

                linhas.pop(i)

                arquivo = open("senhas.txt", "w", encoding="utf-8")

                arquivo.writelines(linhas)

                arquivo.close()

                atualizar_lista()

                resultado.config(text="Cadastro removido!")

                return

        resultado.config(text="Cadastro não encontrado.")

    except:

        resultado.config(text="Nenhum cadastro.")

# ---------------- BOTÕES ----------------

Button(janela, text="Mostrar", command=mostrar).grid(row=5, column=1)

Button(janela, text="Retirar", command=retirar).grid(row=5, column=0)

resultado = Label(janela, text="")
resultado.grid(row=6, column=0, columnspan=2, pady=20)

# Carrega os cadastros existentes
atualizar_lista()

janela.mainloop()