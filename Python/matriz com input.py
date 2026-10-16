turma=[]

linha=int(input("quantas linhas terão a matriz: "))
coluna=int(input("quantas colunas terão a matriz: "))

for i in range(linha):
    linha=[]
    for j in range(coluna):
        linha.append(int(input("digite a nota["+str(i)+","+str(j) + "]:  " )))
    turma.append(linha)
print(turma)
print(turma[1][1])