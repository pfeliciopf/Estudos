# configurações
import random
import time

# estoque = {nome_do_produto: quantidade}
estoque = {}


# --- funções auxiliares ---
def ler_inteiro(mensagem):
    """Só retorna quando o usuário digitar um número válido."""
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit():
            return int(valor)
        print("Digite um número válido, por favor.")


def ler_sim_nao(mensagem):
    """Só aceita 'sim' ou 'não'."""
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ("sim", "não", "nao"):
            return resposta
        print("Responda apenas 'sim' ou 'não'.")


def roleta_descontos():
    lista_descontos = [5, 10, 15, 20, 25, 30, 40, 50, 0, 0, 0]
    desconto = random.choice(lista_descontos)

    if desconto == 0:
        ter_desconto = False
    else:
        ter_desconto = True

    return desconto, ter_desconto


# --- funções principais ---
def cadastrar_produto():
    print("\n--QUE BOM QUE VC QUER CADASTRAR PRODUTOS--")
    while True:
        nome = input("Nome do produto: ").strip().lower()
        if not nome:
            print("O nome não pode ficar em branco.")
            continue
        quantidade = ler_inteiro(f"Quantidade de '{nome}' para cadastrar: ")

        estoque[nome] = estoque.get(nome, 0) + quantidade
        print(f"'{nome}' cadastrado com sucesso! Total em estoque: {estoque[nome]}")

        if ler_sim_nao("Vc quer cadastrar outro produto? sim/não: ") in ("não", "nao"):
            break


def comprar_produtos():
    print("\n--HORA DE COMPRAR PRODUTOS (reabastecer estoque)--")
    if not estoque:
        print("Ainda não há produtos cadastrados. Cadastre um produto primeiro.")
        return

    mostrar_estoque()
    nome = input("Nome do produto que vc quer comprar/reabastecer: ").strip().lower()
    if nome not in estoque:
        print("Esse produto não existe no estoque. Cadastre-o primeiro.")
        return

    quantidade = ler_inteiro(f"Quantidade de '{nome}' para adicionar: ")
    estoque[nome] += quantidade
    print(f"Produtos adicionados ao estoque com sucesso!!!! Total de '{nome}': {estoque[nome]}")


def vender():
    print("\n--HORA DE VENDER PRODUTOS--")
    if not estoque or all(qtd == 0 for qtd in estoque.values()):
        print("Não tem nenhum produto disponível no estoque.")
        return

    mostrar_estoque()
    nome = input("Nome do produto que vc quer vender: ").strip().lower()

    if nome not in estoque or estoque[nome] <= 0:
        print("Esse produto não está disponível no estoque!!!!")
        return

    preco = float(input("Digite o preço do produto: R$ "))

    desconto, ter_desconto = roleta_descontos()

    if ter_desconto:
        preco = preco - (preco * desconto / 100)

    estoque[nome] -= 1

    print(f"Vc ganhou um desconto de: {desconto}%")
    print(f"Preço final: R$ {preco:.2f}")
    print("Produto vendido com sucesso!!!!")


def mostrar_estoque():
    print("\n--ESTOQUE ATUAL DO MERCADO--")
    if not estoque or all(qtd == 0 for qtd in estoque.values()):
        print("O estoque está vazio.")
        return

    for nome, quantidade in estoque.items():
        if quantidade > 0:
            print(f"- {nome}: {quantidade} unidade(s)")


def relatorio():
    print("\n--RELATORIO DO MERCADO--")
    total_itens = sum(estoque.values())
    total_produtos_diferentes = sum(1 for qtd in estoque.values() if qtd > 0)

    print(f"Quantidade total de itens no estoque: {total_itens}")
    print(f"Quantidade de produtos diferentes: {total_produtos_diferentes}")
    if total_produtos_diferentes > 0:
        mais_estocado = max(estoque, key=estoque.get)
        print(f"Produto com maior quantidade: '{mais_estocado}' ({estoque[mais_estocado]} unidades)")


# --- menu principal ---
def home():
    opcoes = {
        1: vender,
        2: comprar_produtos,
        3: cadastrar_produto,
        4: mostrar_estoque,
        5: relatorio,
    }

    while True:
        print("\n===MERCADO===")
        print("1-Vender")
        print("2-Comprar produtos")
        print("3-Cadastrar produtos")
        print("4-Mostrar estoque")
        print("5-Relatorio")
        print("6-Sair")

        pergunta_home = ler_inteiro("Qual função vc vai usar? ")

        if pergunta_home == 6:
            print("Saindo... até logo!")
            break
        elif pergunta_home in opcoes:
            opcoes[pergunta_home]()
            print("\n(voltando ao menu em 5 segundos...)")
            time.sleep(5)  # tempo pra ler a resposta
        else:
            print("DIGITE UMA OPÇÃO VÁLIDA (1 a 6)!!!!")


# Inicializa o programa
if __name__ == "__main__":
    home()