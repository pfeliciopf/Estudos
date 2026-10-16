def transformar_em_hash(texto):
    """Sua lógica original: transforma letras em números"""
    tabela = {
        "A": 2, "B": 2, "C": 2,
        "D": 3, "E": 3, "F": 3,
        "G": 4, "H": 4, "I": 4,
        "J": 5, "K": 5, "L": 5,
        "M": 6, "N": 6, "O": 6,
        "P": 7, "Q": 7, "R": 7, "S": 7,
        "T": 8, "U": 8, "V": 8,
        "W": 9, "X": 9, "Y": 9, "Z": 9
    }
    
    resultado = ""
    for i in texto.upper():
        if i in tabela:
            resultado += str(tabela[i])
        else:
            resultado += i 
    return resultado

# --- SIMULAÇÃO DO SISTEMA ---

print("=== CADASTRO DE CONTA ===")
usuario_cadastrado = input("Defina seu nome de usuário: ")
senha_real = input("Defina sua senha (letras e números): ")

# Salva a senha "criptografada" (o hash)
senha_hash_salva = transformar_em_hash(senha_real)

print("\n--- Conta criada com sucesso! ---")
print(f"O que foi salvo no banco: {senha_hash_salva}")
print("-" * 30)

print("\n=== ÁREA DE LOGIN ===")
tentativa_usuario = input("Usuário: ")
tentativa_senha = input("Senha: ")

# Transformamos a senha digitada agora para comparar com a salva
hash_tentativa = transformar_em_hash(tentativa_senha)

if tentativa_usuario == usuario_cadastrado and hash_tentativa == senha_hash_salva:
    print("\nLogin realizado com sucesso! Bem-vindo.")
else:
    print("\n Erro: Usuário ou senha incorretos.")