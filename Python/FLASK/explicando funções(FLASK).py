from flask import *
import random
import time

app = Flask(__name__)

funcoes = [
    "print() -> Exibe uma mensagem na tela.",
    "input() -> Recebe dados do usuário.",
    "len() -> Retorna o tamanho de uma lista, string, etc.",
    "type() -> Mostra o tipo de uma variável.",
    "range() -> Gera uma sequência de números.",
    "int() -> Converte para inteiro.",
    "float() -> Converte para número decimal.",
    "str() -> Converte para texto."
]

@app.route("/")
def inicio():
    return """
    Bem-vindo!

    Acesse:
    /funcao  -> Mostra uma função aleatória
    /todas   -> Mostra todas as funções
    """

@app.route("/funcao")
def funcao():
    time.sleep(2)
    return random.choice(funcoes)

@app.route("/todas")
def todas():
    time.sleep(2)
    return "\n".join(funcoes)

if __name__ == "__main__":
    app.run(debug=True)