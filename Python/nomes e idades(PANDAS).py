import pandas as pd

quantidade = int(input("Quantos alunos? "))

nomes = []
idades = []
notas = []

for i in range(quantidade):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota: "))

    nomes.append(nome)
    idades.append(idade)
    notas.append(nota)

tabela = pd.DataFrame({
    "Nome": nomes,
    "Idade": idades,
    "Nota": notas
})

print(tabela)