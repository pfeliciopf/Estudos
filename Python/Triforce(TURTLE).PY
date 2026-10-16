from turtle import *
from time import sleep

speed(3)
pensize(4)
bgcolor("black")

def triangulo(x, y, lado):
    penup()
    goto(x, y)
    setheading(0)
    pendown()

    color("gold", "yellow")

    begin_fill()
    for i in range(3):
        forward(lado)
        left(120)
    end_fill()

lado = 150
altura = lado * 0.866

# Triângulo de cima
triangulo(-lado/2, 0, lado)
sleep(0.5)

# Triângulo inferior esquerdo
triangulo(-lado, -altura, lado)
sleep(0.5)

# Triângulo inferior direito
triangulo(0, -altura, lado)

hideturtle()
done()