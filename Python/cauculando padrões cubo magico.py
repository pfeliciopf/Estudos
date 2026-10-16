def calcular_combinacoes(tipo):
    combinacoes = {
        2: 3674160,
        3: 43252003274489856000,
        4: 7401196841564901869874093974498574336000000000,
        5: 282870942277741856536180333107150328293127731985672134721536000000000000000
    }
    return combinacoes.get(tipo, 0)

def main():
    print("--- Comparador de Cubo Mágico vs Burj Khalifa ---")
    
    try:
        tipo = int(input("Qual o tipo do cubo mágico? (2x2, 3x3, 4x4 ou 5x5 (responda, 1, 2, 3, 4, 5)): "))
        if tipo not in [2, 3, 4, 5]:
            print("Por favor, escolha entre 2, 3, 4 ou 5.")
            return

        altura_mm = float(input(f"Qual a altura do seu cubo {tipo}x{tipo} em mm? "))
        
        possibilidades = calcular_combinacoes(tipo)
        
        altura_total_mm = possibilidades * altura_mm
        altura_total_metros = altura_total_mm / 1000
        burj_khalifa_m = 828
        
        quantidade_burjs = altura_total_metros / burj_khalifa_m
        
        print(f"\n--- Resultados para o Cubo {tipo}x{tipo} ---")
        print(f"Número de possibilidades: {possibilidades:,}")
        print(f"Se empilharmos todos, a altura seria de: {altura_total_metros:.2e} metros.")
        print(f"Isso equivale a aproximadamente {quantidade_burjs:.2e} prédios Burj Khalifa!")
        
        if quantidade_burjs > 1000000:
            print("\nCuriosidade: Essa pilha chegaria facilmente a outras galáxias!")

    except ValueError:
        print("Erro: Por favor, digite apenas números.")

if __name__ == "__main__":
    main()
