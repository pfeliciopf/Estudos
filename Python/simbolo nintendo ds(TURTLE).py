import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(4)

turtle.bgcolor("white")

def quadrado_arredondado(x, y, largura, altura, raio):
    t.penup()
    t.goto(x + raio, y)
    t.setheading(0)
    t.pendown()

    for _ in range(2):
        t.forward(largura - 2 * raio)
        t.circle(raio, 90)
        t.forward(altura - 2 * raio)
        t.circle(raio, 90)

# Logo DS (dois quadrados)
quadrado_arredondado(-40, 40, 80, 60, 10)
quadrado_arredondado(-40, -40, 80, 60, 10)

# Nintendo
t.penup()
t.goto(-55, -95)
t.pendown()
t.write("Nintendo", font=("Arial", 18, "bold"))

# DS Lite
t.penup()
t.goto(-55, -135)
t.pendown()
t.write("DS Lite", font=("Arial", 30, "bold"))

turtle.done()