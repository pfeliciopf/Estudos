def horario():
    hora= int(input("hora: "))
    minuto= int(input("minuto: "))
    segundo= int(input("segundo: "))

    horassegundos= (hora*60)*60
    minutosegundos= (minuto*60)

    soma= (horassegundos+minutosegundos+segundo)

    print (f"o horario digitado é equivalente a {soma} segundos")

horario()
