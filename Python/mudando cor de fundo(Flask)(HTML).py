from flask import *
app=Flask(__name__)

@app.route("/")
def mudar_de_cor():
    return """
<!DOCTYPE html>
<html>
<body>
    <h1>Chato não?</h1>
    <p>Está achando esse fundo muito chato? Nosso querido dev nao quer aprender css, então o minimo que ele pode faser é mudar a cor do fundo. </p>
    <p>Escolha abaixo qual cor vc quer</p>
  <button type="button" onclick="document.body.style.backgroundColor = 'yellow'">Amarelo</button>
  <button type="button" onclick="document.body.style.backgroundColor = 'black'">Preto</button>
  <button type="button" onclick="document.body.style.backgroundColor = 'pink'">Rosa</button>
  <button type="button" onclick="document.body.style.backgroundColor = 'blue'">Azul</button>    
  <button type="button" onclick="document.body.style.backgroundColor = 'orange'">laranja</button>
  <button type="button" onclick="document.body.style.backgroundColor = 'red'">Vermelho</button>  
</body>
</html>
    """

if __name__== ("__main__"):
    app.run(debug=True)