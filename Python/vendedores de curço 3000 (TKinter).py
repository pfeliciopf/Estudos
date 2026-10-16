from tkinter import *

def exibir1():
    resultado_botão.config(text="Bom dia, vc pode comprar meu curço por apenas 15x de 1400 reais e aprender a fazewr 400000000 de reais por hora, não acredite neses vendedores ai de baixo")

def exibir2():
    resultado_botão2.config(text="Bom dia, vc pode comprar meu curço por apenas 15x de 1400 reais e aprender a fazewr 400000000 de reais por hora, não acredite neses vendedores ai de cima")

janela= Tk()
janela.title ("texto")
janela.geometry ("900x200")

texto1= Label(janela, text= "clique nesse botão e verá uma incrivel e legal mensagem")
texto1.grid(column = 0, row=0)

texto2= Label(janela, text= "clicando nesse botão sua vida mudara")
texto2.grid(column = 0, row=1)

botao1= Button(janela, text= "Clique aq e sua vida mudara", command = exibir1)
botao1.grid(column = 0, row=2)

resultado_botão= Label(janela, text="")
resultado_botão.grid(column = 0, row=3)

texto3= Label(janela, text= "clicando nesse outro botao a sua vida tambem pode mudar")
texto3.grid(column = 0, row=4)

botao2= Button(janela, text= "Clique aq e sua vida mudara", command = exibir2)
botao2.grid(column = 0, row=5)

resultado_botão2= Label(janela, text="")
resultado_botão2.grid(column = 0, row=6)

janela.mainloop()
