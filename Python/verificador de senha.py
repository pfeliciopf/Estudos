senha = input("Digite a senha: ")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_underline = False
tem_ponto= False
tem_arroba= False

for caractere in senha:
    if caractere == "_":
        tem_underline = True
        print("Achei um underline! Bom.")
    elif caractere == ".":
        tem_ponto = True
    elif caractere == "@":
        tem_arroba==True
    elif caractere in "0123456789":
        tem_numero = True
        print(f"Achei o número {caractere}! Bom.")

    elif caractere in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        tem_maiuscula = True
        print(f"Achei a letra maiúscula {caractere}! Bom.")

    elif caractere in "abcdefghijklmnopqrstuvwxyz":
        tem_minuscula = True
        print(f"Achei a letra minúscula {caractere}! Bom.")

print("\n--- Resultado ---")
if tem_maiuscula and tem_minuscula and tem_numero and tem_underline and tem_ponto and tem_arroba:
    print("Senha perfeita!")
else:
    print("Senha fraca, faltam critérios.")
