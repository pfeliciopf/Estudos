import random

def gerar_embaralhamento(tamanho=20):
    movimentos_disponiveis = [
        "R", "R'", "R2", "L", "L'", "L2",
        "U", "U'", "U2", "D", "D'", "D2",
        "F", "F'", "F2", "B", "B'", "B2"
    ]
    
    embaralhamento = []
    
    while len(embaralhamento) < tamanho:
        novo_movimento = random.choice(movimentos_disponiveis)
        
        if len(embaralhamento) > 0:
            ultimo_movimento = embaralhamento[-1]
            if novo_movimento[0] == ultimo_movimento[0]:
                continue
                
        embaralhamento.append(novo_movimento)
        
    return ' '.join(embaralhamento)

try:
    quantidade = int(input("Quantos embaralhamentos você deseja gerar? "))
    print("\n--- SEUS EMBARALHAMENTOS ---")
    
    for i in range(quantidade):
        scramble = gerar_embaralhamento()
        print(f"{i + 1}-> {scramble}")
        
except ValueError:
    print("Por favor, digite um número inteiro válido.")
