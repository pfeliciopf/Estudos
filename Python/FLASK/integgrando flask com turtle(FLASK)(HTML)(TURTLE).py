from flask import Flask
import turtle

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Turtle</title>
</head>
<body>
    <h1>Turtle</h1>

    <form action="/desenhar">
        <button>Desenhar</button>
    </form>
</body>
</html>
"""


@app.route("/")
def home():
    return html


@app.route("/desenhar")
def desenhar():
    t = turtle.Turtle()
    t.speed(0)
    turtle.bgcolor("black")

    cores = ["red", "black"]

    for x in range(3600):
        t.pencolor(cores[x % len(cores)])
        t.forward(x * 1.5)
        t.left(87)

    return html


app.run()