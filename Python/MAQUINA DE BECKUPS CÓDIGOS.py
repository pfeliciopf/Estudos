import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk


# Extensões que serão copiadas
extensoes = [
    ".py",
    ".c",
    ".cpp",
    ".h",
    ".hpp",
    ".java",
    ".js",
    ".html",
    ".css",
    ".php",
    ".rb",
    ".go",
    ".rs",
    ".sh",
    ".sql",
    ".lua",
    ".gd",
    ".cs",
    ".json"
]

pasta_origem = ""
pasta_destino = ""


def escolher_origem():

    global pasta_origem

    pasta = filedialog.askdirectory(
        title="Escolha a pasta dos códigos"
    )

    if pasta:
        pasta_origem = pasta

        origem_texto.config(
            text=f"Origem:\n{pasta}"
        )


def escolher_destino():

    global pasta_destino

    pasta = filedialog.askdirectory(
        title="Escolha onde salvar o backup"
    )

    if pasta:
        pasta_destino = pasta

        destino_texto.config(
            text=f"Destino:\n{pasta}"
        )


def iniciar_backup():

    global pasta_origem
    global pasta_destino

    # Verifica a origem
    if not pasta_origem:

        messagebox.showwarning(
            "Atenção",
            "Escolha primeiro a pasta dos códigos."
        )

        return

    # Verifica o destino
    if not pasta_destino:

        messagebox.showwarning(
            "Atenção",
            "Escolha primeiro onde salvar o backup."
        )

        return

    # Pega o nome digitado
    nome_backup = nome_entry.get().strip()

    if not nome_backup:

        messagebox.showwarning(
            "Atenção",
            "Digite um nome para o backup."
        )

        return

    # Remove caracteres que não podem ser usados em nomes de pasta
    caracteres_invalidos = '<>:"/\\|?*'

    if any(c in nome_backup for c in caracteres_invalidos):

        messagebox.showwarning(
            "Nome inválido",
            "O nome do backup possui caracteres inválidos."
        )

        return

    fazer_backup(
        pasta_origem,
        pasta_destino,
        nome_backup
    )


def fazer_backup(origem, destino, nome_backup):

    # Pasta onde o backup será criado
    pasta_backup = os.path.join(
        destino,
        nome_backup
    )

    # Se já existir
    if os.path.exists(pasta_backup):

        resposta = messagebox.askyesno(
            "Backup já existente",
            f"O backup '{nome_backup}' já existe.\n\n"
            "Deseja substituir esse backup?"
        )

        if resposta:

            try:
                shutil.rmtree(pasta_backup)

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    f"Não foi possível substituir o backup.\n\n{erro}"
                )

                return

        else:

            messagebox.showinfo(
                "Escolha outro nome",
                "Digite outro nome para o backup."
            )

            nome_entry.focus()

            return

    # Cria a pasta
    os.makedirs(pasta_backup)

    botao.config(state="disabled")

    # Procura os arquivos
    arquivos = []

    for raiz, pastas, nomes in os.walk(origem):

        for nome in nomes:

            extensao = os.path.splitext(nome)[1].lower()

            if extensao in extensoes:

                arquivos.append(
                    os.path.join(raiz, nome)
                )

    total = len(arquivos)

    # Nenhum arquivo encontrado
    if total == 0:

        texto.config(
            text="Nenhum código encontrado."
        )

        barra["value"] = 0

        botao.config(state="normal")

        messagebox.showinfo(
            "Backup",
            "Nenhum arquivo de código foi encontrado."
        )

        # Remove o backup vazio
        os.rmdir(pasta_backup)

        return

    # Configura a barra
    barra["maximum"] = total
    barra["value"] = 0

    # Copia os arquivos individualmente
    for numero, arquivo in enumerate(arquivos, 1):

        nome = os.path.basename(arquivo)

        destino_arquivo = os.path.join(
            pasta_backup,
            nome
        )

        # Evita arquivos com o mesmo nome
        contador = 1

        nome_base, extensao = os.path.splitext(nome)

        while os.path.exists(destino_arquivo):

            novo_nome = (
                f"{nome_base}_{contador}{extensao}"
            )

            destino_arquivo = os.path.join(
                pasta_backup,
                novo_nome
            )

            contador += 1

        # Copia o arquivo
        shutil.copy2(
            arquivo,
            destino_arquivo
        )

        # Atualiza a interface
        texto.config(
            text=f"Copiando:\n{nome}\n\n"
                 f"{numero} de {total} códigos"
        )

        barra["value"] = numero

        janela.update_idletasks()

    # Finalizado
    texto.config(
        text=f"Backup concluído!\n\n"
             f"{total} códigos copiados."
    )

    botao.config(state="normal")

    messagebox.showinfo(
        "Backup concluído",
        f"Backup '{nome_backup}' concluído!\n\n"
        f"{total} arquivos foram copiados."
    )


# -------------------------
# JANELA
# -------------------------

janela = tk.Tk()

janela.title("Backup de Códigos")

janela.geometry("550x430")

janela.resizable(False, False)


# Título
titulo = tk.Label(
    janela,
    text="Backup de Códigos",
    font=("Arial", 16)
)

titulo.pack(pady=(20, 5))


# Texto
texto = tk.Label(
    janela,
    text="Escolha as opções do backup",
    font=("Arial", 11)
)

texto.pack(pady=(0, 15))


# -------------------------
# ORIGEM
# -------------------------

botao_origem = tk.Button(
    janela,
    text="ESCOLHER PASTA DOS CÓDIGOS",
    command=escolher_origem,
    font=("Arial", 10),
    width=30
)

botao_origem.pack()


origem_texto = tk.Label(
    janela,
    text="Origem: nenhuma pasta selecionada",
    font=("Arial", 9),
    fg="gray",
    wraplength=500
)

origem_texto.pack(pady=(5, 15))


# -------------------------
# DESTINO
# -------------------------

botao_destino = tk.Button(
    janela,
    text="ESCOLHER ONDE SALVAR",
    command=escolher_destino,
    font=("Arial", 10),
    width=30
)

botao_destino.pack()


destino_texto = tk.Label(
    janela,
    text="Destino: nenhuma pasta selecionada",
    font=("Arial", 9),
    fg="gray",
    wraplength=500
)

destino_texto.pack(pady=(5, 15))


# -------------------------
# NOME DO BACKUP
# -------------------------

nome_label = tk.Label(
    janela,
    text="Nome do backup:"
)

nome_label.pack()


nome_entry = tk.Entry(
    janela,
    width=35,
    font=("Arial", 10)
)

nome_entry.pack(pady=(3, 15))

nome_entry.insert(
    0,
    "BACKUP_CODIGOS"
)


# -------------------------
# BOTÃO
# -------------------------

botao = tk.Button(
    janela,
    text="FAZER BACKUP",
    command=iniciar_backup,
    font=("Arial", 11),
    width=20
)

botao.pack()


# -------------------------
# BARRA
# -------------------------

barra = ttk.Progressbar(
    janela,
    length=450,
    mode="determinate"
)

barra.pack(pady=20)


janela.mainloop()

