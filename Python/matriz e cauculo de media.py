turma = [[5.0, 4.5, 7.0, 5.2, 6.1],
         [2.1, 6.5, 8.0, 7.0, 6.7],
         [8.6, 7.0, 9.1, 8.7, 9.3]]


for i in range(3):
    media = 0

    for j in range(5):
        media = media + turma[i][j]

    media = media / 5

    print("Media do aluno", i + 1, "=", media)

for j in range(5):
    media = 0

    for i in range(3):
        media = media + turma[i][j]

    media = media / 3

    print("Media da materia", j + 1, "=", media)
