import sqlite3

conexao = sqlite3.connect("museu.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    obra TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL
)
""")

while True:
    try:
        obra = input("Digite o nome da obra: ")
        autor = input("Digite o autor(a): ")
        ano = int(input("em que ano foi lançado a obra?:  "))

        cursor.execute(
            """
            INSERT INTO livros
            (obra, autor, ano)
            VALUES (?, ?, ?)
            """,
            (obra, autor, ano)
        )

        conexao.commit()
        print("obra cadastrado com sucesso!")

    except ValueError:
        print("Erro: Entrada inválida.")

    sair = input("Deseja cadastrar outra obra? (s/n): ").lower()

    if sair != 's':
        break

conexao.close()