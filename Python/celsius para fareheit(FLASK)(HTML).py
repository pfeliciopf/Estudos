from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def conversor():
    resultado = ""
    
    if request.method == "POST":
        celsius_texto = request.form.get("celsius")
        
        if celsius_texto:
            celsius = float(celsius_texto)
            fahrenheit = (celsius * 9 / 5) + 32
            resultado = f"Resultado: {fahrenheit} °F"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Conversor Flask</title>
    </head>
    <body>

        <h1>Conversor de Celsius para Fahrenheit no Flask</h1>
        
        <form method="POST">
            <p>Digite a temperatura em Celsius:</p>
            <input type="number" name="celsius" step="any" required>
            <button type="submit">Converter</button>
        </form>
        
        <h2>{resultado}</h2>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
