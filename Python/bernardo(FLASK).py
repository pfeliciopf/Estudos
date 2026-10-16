from flask import *

app=Flask(__name__)

@app.route("/")
def home():
    return "bom dia bernardo"
@app.route("/bernardodete")
def bernardo():
    return "meu nome é bernardo, gosto do tiktok shop"

if __name__== "__main__":
    app.run(debug=True)
