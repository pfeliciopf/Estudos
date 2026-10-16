import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

# Paleta quente
cores = [
    "red", 
    "black"
]

for x in range(3600):
    t.pencolor(cores[x % len(cores)])
    t.forward(x * 1.5)
    t.left(87)

turtle.done()


