import requests
from tkinter import *

# ---------------- Função ---------------- #

def calcular():
    try:
        # Busca a Selic
        url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json"
        selic = float(requests.get(url).json()[0]["valor"].replace(",", "."))

        valor = float(entry_valor.get())
        percentual = float(entry_percentual.get())

        # Aproximação: CDI ≈ Selic
        taxa = (selic / 100) * (percentual / 100)

        ganho_ano = valor * taxa
        ganho_mes = ganho_ano / 12
        ganho_semana = ganho_ano / 52
        ganho_dia = ganho_ano / 365

        resultado.config(
            text=
            f"Selic atual: {selic:.2f}%\n\n"
            f"Taxa do CDB: {taxa*100:.2f}% ao ano\n\n"
            f"Ganho por dia: R$ {ganho_dia:.2f}\n"
            f"Ganho por semana: R$ {ganho_semana:.2f}\n"
            f"Ganho por mês: R$ {ganho_mes:.2f}\n"
            f"Ganho por ano: R$ {ganho_ano:.2f}"
        )

    except:
        resultado.config(text="Digite valores válidos!")

# ---------------- Janela ---------------- #

janela = Tk()
janela.title("Calculadora de CDB")
janela.geometry("400x330")

Label(janela, text="Valor investido (R$)").grid(row=0, column=0, padx=10, pady=5)

entry_valor = Entry(janela)
entry_valor.grid(row=0, column=1, padx=10, pady=5)

Label(janela, text="% do CDI").grid(row=1, column=0, padx=10, pady=5)

entry_percentual = Entry(janela)
entry_percentual.grid(row=1, column=1, padx=10, pady=5)

Button(janela,
       text="Calcular",
       command=calcular,
       width=20).grid(row=2, column=0, columnspan=2, pady=10)

resultado = Label(janela, text="", justify=LEFT, font=("Arial", 10))
resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

janela.mainloop()