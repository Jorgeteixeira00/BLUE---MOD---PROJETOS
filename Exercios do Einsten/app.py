from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Olá Jorge</h1>"

@app.route('/Einsten')
def Einsten():
    nome = "Betão"
    sobrenome = "Einstein"
    idade = 41
    imagem_doidao = ("/static/Albert Einstein_ quem foram seus filhos e o que aconteceu com eles_.jpg")
    imagem_lucida = ("/static/albert-einstein-wikipedia-int.jpg")
    return render_template("index.html", nome=nome, sobrenome=sobrenome, idade=idade, imagem_doidao=imagem_doidao, imagem_lucido=imagem_lucida)

if (__name__ == "__main__"):
    app.run(debug=True)