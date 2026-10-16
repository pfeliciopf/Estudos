import random
from tkinter import *

def gerar_embaralhamento(tamanho=20):
    movimentos_disponiveis = [
        "R", "R'", "R2", "L", "L'", "L2",
        "U", "U'", "U2", "D", "D'", "D2",
        "F", "F'", "F2", "B", "B'", "B2"
    ]
    embaralhamento = []
    while len(embaralhamento) < tamanho:
        novo_movimento = random.choice(movimentos_disponiveis)
        if len(embaralhamento) > 0:
            if novo_movimento[0] == embaralhamento[-1][0]:
                continue
        embaralhamento.append(novo_movimento)
    return ' '.join(embaralhamento)

def acao_do_botao():
    # Pega o texto gerado e coloca dentro da caixa de texto
    scramble = gerar_embaralhamento()
    campo_texto.delete("1.0", END)
    campo_texto.insert("1.0", scramble)

# --- CONFIGURAÇÃO DA JANELA ---
janela = Tk()
janela.title("Scramble")

# --- ELEMENTOS DA INTERFACE (2 linhas por elemento) ---

# Texto de instrução
lbl_instrucao = Label(janela, text="Clique no botão para gerar um scramble:")
lbl_instrucao.grid(row=0, column=0, padx=10, pady=5)

# Botão que chama a função
btn_gerar = Button(janela, text="Gerar Scramble", command=acao_do_botao)
btn_gerar.grid(row=1, column=0, padx=10, pady=5)

# Caixa de texto que exibe o resultado
campo_texto = Text(janela, width=40, height=3, wrap=WORD)
campo_texto.grid(row=2, column=0, padx=10, pady=10)

# Inicia a janela
janela.mainloop()