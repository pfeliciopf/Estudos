import sqlite3

conexao = sqlite3.connect("livros.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    livro TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL
)
""")

while True:
    try:
        livro = input("Digite o nome do livro: ")
        autor = input("Digite o autor(a): ")
        ano = int(input("em que ano foi lançado o livro?: ? "))

        cursor.execute(
            """
            INSERT INTO livros
            (livro, autor, ano)
            VALUES (?, ?, ?)
            """,
            (livro, autor, ano)
        )

        conexao.commit()
        print("livro cadastrado com sucesso!")

    except ValueError:
        print("Erro: Entrada inválida.")

    sair = input("Deseja cadastrar outro livro? (s/n): ").lower()

    if sair != 's':
        break

conexao.close()