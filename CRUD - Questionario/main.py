from flask import Flask, render_template, request
from db import db
from models import Contato

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dados.db"
db.init_app(app)

#criando a funcao para chamar o html
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if request.method == "GET":
        return render_template("registrar_contato.html")
    
    elif request.method == "POST":
        nome = request.form["nomeForm"]
        telefone = request.form["telefoneForm"]
        print(nome)
        print(telefone)
        return "Usuario Registrado"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run (debug=True)