lista_total = []

def home():
    while True:
        print("\n1- Adicionar item")
        print("2- Retirar item")
        print("3- Ver lista")
        print("4- SAIR")

        pergunta_home = int(input("O QUE DESEJA?: "))

        if pergunta_home == 1:
            adicionar_i()

        elif pergunta_home == 2:
            retirar_i()

        elif pergunta_home == 3:
            ver_lista()

        elif pergunta_home == 4:
            break

        else:
            print("Opção inválida!")

def adicionar_i():
    pergunta_a_i = int(input("Quantos itens gostaria de adicionar?: "))

    for i in range(pergunta_a_i):
        item_p_add = input(f"Item {i+1}: ")
        lista_total.append(item_p_add)

def retirar_i():
    if len(lista_total) == 0:
        print("Não tem o que remover")
        return

    print("\nLista de itens:")
    for i, item in enumerate(lista_total, start=1):
        print(f"{i}- {item}")

    pertgunta_r_i = int(input("Qual item gostaria de retirar?: "))

    lista_total.pop(pertgunta_r_i - 1)
    print("Item removido!")

def ver_lista():
    if len(lista_total) == 0:
        print("Não tem nada na lista")
        return

    print("\nLista de itens:")
    for i, item in enumerate(lista_total, start=1):
        print(f"{i}- {item}")

home()