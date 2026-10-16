from flask import Flask, request, redirect

app = Flask(__name__)

# Página inicial
@app.route("/")
def inicio():
    return """
    <h1>Bloco de Notas</h1>

    <a href="/adicionar">Adicionar nota</a>
    <br>
    <a href="/notas">Ver notas</a>
    """


# Adicionar nota
@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():

    if request.method == "POST":
        nota = request.form["nota"]

        with open("notas.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(nota + "\n")

        return redirect("/notas")

    return """
    <h1>Adicionar nota</h1>

    <form method="POST">
        <input type="text" name="nota">
        <button>Salvar</button>
    </form>

    <a href="/">Voltar</a>
    """


# Mostrar notas
@app.route("/notas")
def mostrar_notas():

    try:
        with open("notas.txt", "r", encoding="utf-8") as arquivo:
            notas = arquivo.readlines()
    except FileNotFoundError:
        notas = []

    html = "<h1>Minhas notas</h1>"

    for i, nota in enumerate(notas):
        html += f"""
        <p>
            {nota}
            <a href="/remover/{i}">Remover</a>
        </p>
        """

    html += '<br><a href="/">Voltar</a>'

    return html


# Remover nota
@app.route("/remover/<int:indice>")
def remover(indice):

    with open("notas.txt", "r", encoding="utf-8") as arquivo:
        notas = arquivo.readlines()

    if 0 <= indice < len(notas):
        notas.pop(indice)

    with open("notas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(notas)

    return redirect("/notas")


app.run(debug=True)