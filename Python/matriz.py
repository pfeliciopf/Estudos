turma=[]
for i in range(5):
    linha=[]
    for j in range(5):
        linha.append(int(input("digite a nota["+str(i)+","+str(j) + "]:  " )))
    turma.append(linha)
print(turma)
print(turma[1][1])