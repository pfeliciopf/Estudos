import sqlite3

conexao = sqlite3.connect("arquivo.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contas_bancarias (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titular TEXT NOT NULL,
    saldo FLOAT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    ano_criacao INTEGER NOT NULL,
    idade INTEGER NOT NULL
)
""")

while True:
    try:
        titular = input("Digite o nome do titular: ")
        saldo = float(input("Digite o saldo: "))
        cpf = input("Digite o CPF: ")
        ano_criacao = int(input("Em que ano foi criada essa conta?: "))
        idade = int(input("Qual a idade do titular? "))

        cursor.execute(
            """
            INSERT INTO contas_bancarias
            (titular, saldo, cpf, ano_criacao, idade)
            VALUES (?, ?, ?, ?, ?)
            """,
            (titular, saldo, cpf, ano_criacao, idade)
        )

        conexao.commit()
        print("Conta cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: Este CPF já está cadastrado.")

    except ValueError:
        print("Erro: Entrada inválida.")

    sair = input("Deseja cadastrar outra conta? (s/n): ").lower()

    if sair != 's':
        break

conexao.close()

