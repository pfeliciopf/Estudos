from tkinter import *

def conta():
    while True:
        soma=1+1
        print(soma)
    

janela=Tk()
janela.geometry("400x400")

texto1=Label(text="aperte o botao e veja o terminal")
texto1.grid(column=0,row=1)

botao=button(text="aperte aqui!!!", command=conta)
botao.grid(column=0, row=1)

janela.mainloop()