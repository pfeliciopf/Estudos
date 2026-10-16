peso = float (input("qual o peso: "))
altura= float (input("qual o peso: "))
resultado= peso/(altura**2)

print (resultado)
if resultado <18.5:
    print ("abaixo do peso")

elif resultado <25:
    print ("adequado")

elif resultado <30:
    print ("acima do peso")

