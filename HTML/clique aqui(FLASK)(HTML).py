from flask import Flask

app = Flask(__name__)

mensagem = "Olá, este é um projeto Flask simples!"

@app.route("/")
def inicio():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Meu Flask</title>
    </head>
    <body>

        <h1>Meu Primeiro projeto com pyhon Flask e HTML</h1>

        <p>{mensagem}</p>

        <form action="/botao" method="post">
            <button type="submit">Clique aqui</button>
        </form>

    </body>
    </html>
    """


@app.route("/botao", methods=["POST"])
def botao():
    global mensagem
    mensagem = "O botão foi clicado! Flask recebeu a requisição."
    return inicio()


if __name__ == "__main__":
    app.run(debug=True)