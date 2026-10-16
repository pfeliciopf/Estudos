lista_nomes = []

while True:
    nome = input("Digite um nome: ")
    
    if nome == "sair":
        break
        
    try:
        numero = float(nome)
        print("Erro: digite um nome valido, nao numeros")
    except ValueError:
        lista_nomes.append(nome)

print("Sua lista de nomes:")
print(lista_nomes)
