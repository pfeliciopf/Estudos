import tkinter as tk

def converter():
    c = float(entrada.get())
    f = (c * 9/5) + 32
    resultado.config(text=f"{f:.1f} °F")

janela = tk.Tk()
janela.title("Conversor")

tk.Label(janela, text="Temperatura em °C").pack()

entrada = tk.Entry(janela)
entrada.pack()

tk.Button(janela, text="Converter", command=converter).pack(pady=5)

resultado = tk.Label(janela, text="")
resultado.pack()

janela.mainloop()