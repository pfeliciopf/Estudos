from tkinter import *


def den_grafica():
    nome_pais = str(nome.get())
    tamanho_pais = float(pais.get())
    gente_pais = int(gente.get())

    dg = (tamanho_pais) / gente_pais

    resultado.config(text=f"a densidade demografica da(o) {nome_pais} é {dg}")


janela = Tk()
janela.geometry("800x200")
janela.title("densidade demofráfica")

texto_apresentacao = Label(janela, text="bom dia, aqui vc pode medir a densidade demografica de qualquer pais. Isso é: a quantidade de gente por metro quadrado ")
texto_apresentacao.grid(column=0, row=0)

textoexplicacao1= Label(janela, text="digite o nome do pais ou lugar")
textoexplicacao1.grid(column=0, row= 1)
nome = Entry(janela)
nome.grid(column=0, row=2)

textoexplicacao2= Label(janela, text="digite o tamanho do pais ou lugar(não é necessario colocar m²)")
textoexplicacao2.grid(column=0, row= 3)
pais = Entry(janela)
pais.grid(column=0, row=4)

textoexplicacao3= Label(janela, text="digite a quantidade de pessoas deste pais ou lugar")
textoexplicacao3.grid(column=0, row= 5)
gente = Entry(janela)
gente.grid(column=0, row=6)

resultado = Label(janela, text="")
resultado.grid(column=0, row=8)

botao= Button(janela, text= "caucule", command= den_grafica)
botao.grid (column= 0, row= 7)

janela.mainloop()