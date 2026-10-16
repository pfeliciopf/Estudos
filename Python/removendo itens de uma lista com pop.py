lista=[
    "1-Pato",
    "2-cachorro",
    "3-gato",
    "4-ovelha",
    "5-sair"
]

while True:
    print(lista)
    pergunta= int(input("qual item da lista vc gostaria de resolver?:  "))
    
    lista.pop(pergunta-1)
    
    if pergunta== 5:
        print("---saindo---")
        break

    print (lista)
