from tkinter import *
from tkinter import messagebox

def senha_usuario():
    # Agora o .get() vai funcionar corretamente
    usuario = str(entrada_usuario.get())
    senha = str(entrada_senha.get())
    
    # Exemplo de validação
    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Sucesso", "Login efetuado!")
    else:
        messagebox.showerror("Erro", "Dados incorretos.")

janela = Tk()
janela.title("Login")
janela.geometry("250x150")

# Texto de boas-vindas
texto1 = Label(janela, text="bom dia")
texto1.grid(column=0, row=0, columnspan=2, pady=10)

# Configuração do Utilizador
label_user = Label(janela, text="Usuário:")
label_user.grid(column=0, row=1)

entrada_usuario = Entry(janela)
entrada_usuario.grid(column=1, row=1)

# Configuração da Senha
label_pass = Label(janela, text="Senha:")
label_pass.grid(column=0, row=2)

entrada_senha = Entry(janela, show="*")
entrada_senha.grid(column=1, row=2)

# Botão para acionar a função
botao = Button(janela, text="Entrar", command=senha_usuario)
botao.grid(column=0, row=3, columnspan=2, pady=10)

janela.mainloop()
