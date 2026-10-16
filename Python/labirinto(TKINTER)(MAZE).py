from tkinter import *
from mazelib import Maze
from mazelib.generate.Prims import Prims

LINHAS = 15
COLUNAS = 15

m = Maze()
m.generator = Prims(LINHAS, COLUNAS)
m.generate()
m.generate_entrances()

grid = m.grid
inicio = m.start
fim = m.end

grid[inicio[0]][inicio[1]] = 0
grid[fim[0]][fim[1]] = 0

TAM_LINHAS = len(grid)
TAM_COLUNAS = len(grid[0])

janela = Tk()
janela.title("Labirinto com mazelib")

quadrados = {}
for linha in range(TAM_LINHAS):
    for coluna in range(TAM_COLUNAS):
        cor = "black" if grid[linha][coluna] == 1 else "white"
        q = Label(janela, width=2, height=1, bg=cor)
        q.grid(row=linha, column=coluna)
        quadrados[(linha, coluna)] = q

quadrados[inicio].config(bg="yellow")
quadrados[fim].config(bg="pink")


def resolver():
    visto = [[False] * TAM_COLUNAS for _ in range(TAM_LINHAS)]
    visto[inicio[0]][inicio[1]] = True
    veio_de = {inicio: None}
    buscar([inicio], visto, veio_de)


def buscar(fila, visto, veio_de):
    if not fila:
        return

    linha, coluna = fila.pop(0)

    if (linha, coluna) not in (inicio, fim):
        # Alterado de lightblue para blue (azul escuro/forte)
        quadrados[(linha, coluna)].config(bg="blue")

    if (linha, coluna) == fim:
        atual = fim
        while atual:
            if atual not in (inicio, fim):
                # Mantido em vermelho para a resolução final
                quadrados[atual].config(bg="red")
            atual = veio_de[atual]
        return

    for dl, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nl, nc = linha + dl, coluna + dc
        if 0 <= nl < TAM_LINHAS and 0 <= nc < TAM_COLUNAS:
            if grid[nl][nc] == 0 and not visto[nl][nc]:
                visto[nl][nc] = True
                veio_de[(nl, nc)] = (linha, coluna)
                fila.append((nl, nc))

    janela.after(10, buscar, fila, visto, veio_de)


Button(janela, text="Resolver", command=resolver).grid(
    row=TAM_LINHAS, column=0, columnspan=TAM_COLUNAS
)

janela.mainloop()
