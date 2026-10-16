while True:
    comando = input("Digite um comando (ou 'sair'): ")
    if comando.lower() == 'sair':
        print("Saindo do loop...")
        break
    print(f"Você digitou: {comando}")
