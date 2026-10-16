while True:
    comando = input("PARA SAIR ESCREVA (SAIR)")
    if comando.lower() == 'sair':
        print("Saindo do loop...")
        break
    print(f"Você digitou: {comando}")
