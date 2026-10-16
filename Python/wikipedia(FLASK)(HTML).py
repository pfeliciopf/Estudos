from flask import *

app= Flask(__name__)

@app.route("/")
def home():
    return """
        <!DOCTYPE html>
        <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Entrando em link</title>
    </head>
    <body>
        <h1>WIKIPEDIA</h1>
        <p>Para entrar no site, clique no link abixo</p>
        <p> <a href="https://wikipedia.com/">Clique aqui!!!</a></p>
    </body>
    </html>
    """
if __name__=="__main__":
    app.run(debug=True)


