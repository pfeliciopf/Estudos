#média por trimestre
robo = str(input("vc quer caucular a sua media em alguma matéria: ")).lower()

if robo == "não":
    print("ok, volte outra hora")

elif robo == "sim":
    p1 = float(input("Qual foi a sua nota na p1: "))
    p2 = float(input("qual foi a sua nota na p2: "))
    pic = float(input("qual foi a sua nota na PIC: "))

    media = (pic*4 + p1*3 + p2*3)/10

    if media < 7:
        print("sua nota nessa média foi:", media, "vc não passou")

    elif media >= 7 and media <= 10:
        print("sua nota nessa média foi:", media, "vc passou")

    else:
        print("ERRO, sua média não pode ser acima de 10")
