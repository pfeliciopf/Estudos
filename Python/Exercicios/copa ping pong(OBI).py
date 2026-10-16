#prova 2018 fase 2

kung= int(input())
lu=int(input())

fase = 0

while kung != lu:
    kung = (kung + 1) // 2
    lu = (lu + 1) // 2
    fase += 1

if fase == 1:
    print("oitavas")
elif fase == 2:
    print("quartas")
elif fase == 3:
    print("semifinal")
else:
    print("final")   