vendas = []
saidas = []

def registrarv():
    valor = float(input("Valor da venda: R$ "))
    vendas.append(valor)
    print("Venda registrada com sucesso!")

def registrars():
    valor = float(input("Valor da saída: R$ "))
    saidas.append(valor)
    print("Saída registrada com sucesso!")

def home():
    while True:
        print("\n===== LOJA =====")
        print("1 - Registrar venda")
        print("2 - Registrar saída")
        print("3 - Fechar loja")

        sistema = int(input("Escolha uma opção: "))

        if sistema == 1:
            registrarv()

        elif sistema == 2:
            registrars()

        elif sistema == 3:
            print("\n===== RESUMO =====")
            print(f"Quantidade de vendas: {len(vendas)}")
            print(f"Total vendido: R$ {sum(vendas):.2f}")
            print(f"Quantidade de saídas: {len(saidas)}")
            print(f"Total de saídas: R$ {sum(saidas):.2f}")
            print(f"Lucro: R$ {sum(vendas) - sum(saidas):.2f}")
            print("Loja fechada.")
            break

        else:
            print("Opção inválida!")

home()
