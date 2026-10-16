nota=float(input("qual a nota"))

if nota >8 and nota <=10:
    print ("bolinha verde")
elif nota >=7 and nota <=8:
    print("bolinha azul")
elif nota >=5 and nota <7:
    print ("bolinha amarela")
elif nota >0 and nota <5:
    print ("bolinha vermelha")
else:
    print ("invalido")
