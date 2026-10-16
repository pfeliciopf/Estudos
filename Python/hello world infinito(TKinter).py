from tkinter import *
import time

contador = 0
inicio = 0

def rodar_contagem():
    global contador, inicio
    
    if contador == 0:
        inicio = time.time()
        
    print(f"{contador}-hello world")
    contador += 1
    
    if contador < 10000000001:
        janela.after(1, rodar_contagem)
    else:
        fim = time.time()
        tempo_total = fim - inicio
        print(f"Tempo total: {tempo_total:.4f} segundos")
        contador = 0

janela = Tk()

texto = Label(text="Bom dia, aperte esse botao e veja o terminal")
texto.grid(column=0, row=0)

botao = Button(text="aperte aq", command=rodar_contagem)
botao.grid(column=0, row=1)

janela.mainloop()
