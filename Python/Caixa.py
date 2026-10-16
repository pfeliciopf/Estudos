dinheiro = 0
def sistema():
    while True:
        print(f"seu saldo é {dinheiro}")    
        pergunta = input("Vc quer adicionar ou retirar dinheiro do caixa? adicionar/retirar: ").upper()
    
        if pergunta == "ADICIONAR":
            quantidade = int(input("Quanto deseja adicionar? "))
            dinheiro += quantidade
            print(f"Adicionado! Saldo atual: R$ {dinheiro}")
    
        elif pergunta == "RETIRAR":
            quantidade = int(input("Quanto deseja retirar? "))
            if quantidade > dinheiro:
                print(f"Saldo insuficiente! Saldo atual: R$ {dinheiro}")
            else:
                dinheiro -= quantidade
                print(f"Retirado! Saldo atual: R$ {dinheiro}")
    
        else:
            print("Opção inválida! Digite 'adicionar' ou 'retirar'.") 

sistema()


