import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    codigo TEXT NOT NULL PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL
)
""")

while True:
    try:
        codigo = input("Digite o código do livro: ")
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor(a): ")
        ano = int(input("Ano de lançamento: "))

        cursor.execute(
            "INSERT INTO livros (codigo, titulo, autor, ano) VALUES (?, ?, ?, ?)",
            (codigo, titulo, autor, ano)
        )
        conexao.commit()
        print("Livro cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: Esse código já existe.")
    except ValueError:
        print("Erro: Ano inválido.")

    if input("Deseja cadastrar outro? (s/n): ").lower() != 's':
        break

conexao.close()