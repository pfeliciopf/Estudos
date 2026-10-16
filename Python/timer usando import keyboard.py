import keyboard
import time

x = input("vc quer começar o timer? sim/não: ").lower()

if x == "sim":
    inicio = time.time()
    print("Pressione 'space' para parar...")

    while True:
        if keyboard.is_pressed('space'):
            fim = time.time()
            print("Tecla 'space' pressionada!")
            print("Tempo decorrido:", fim - inicio, "segundos")
            break
else:
    print("Timer não iniciado.")

