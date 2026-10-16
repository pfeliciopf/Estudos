import calendar

ano=int(input())
mes=int(input())
dia=int(input())

dia_semana=calendar.weekday(ano, mes, dia)

if dia_semana==0:
    print("segunda")
elif dia_semana==1:
    print("terça")
elif dia_semana==2:
    print("quarta")
elif dia_semana==3:
    print("quinta")
elif dia_semana==4:
    print("sexta")
elif dia_semana==5:
    print("sabado")
else:
    print("domingo")