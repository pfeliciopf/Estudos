import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

# Paleta quente
cores = [
    "#FF0000",  # vermelho
    "#FF4500",  # vermelho-laranja
    "#FF6A00",  # laranja
    "#FF8C00",  # laranja escuro
    "#FFD000",  # amarelo
    "#FFB000",  # dourado
    "#E63946",  # vermelho coral
    "#C9184A"   # rosa avermelhado
]

for x in range(3600):
    t.pencolor(cores[x % len(cores)])
    t.forward(x * 1.5)
    t.left(87)

turtle.done()


