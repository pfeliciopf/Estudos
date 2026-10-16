from flask import Flask

app = Flask(__name__)

contador = 0

@app.route("/")
def inicio():
    global contador

    return f"""
    <html>
        <head>
            <title>Contador Flask</title>
        </head>

        <body>

            <h1>Contador de Cliques</h1>

            <h2>{contador}</h2>

            <form action="/somar" method="post">
                <button>Clique aqui!</button>
            </form>

        </body>
    </html>
    """

@app.route("/somar", methods=["POST"])
def somar():
    global contador
    contador += 1

    return """
    <script>
        window.location.href = "/";
    </script>
    """

app.run(debug=True)