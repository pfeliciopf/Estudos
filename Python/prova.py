dificeis= 8
faceis=2
medias=5

q1= int(input("quantas questões faceis o aluno acertou: "))
q2= int(input("quantas questões medias o aluno acertou: "))
q3= int(input("quantas questões dificeis o aluno acertou: "))

pontuacao= q1*2+q2*5+q3*8
print (f"sua pontuação foi {pontuacao}")