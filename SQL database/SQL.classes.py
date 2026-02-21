#importando o flask
from flask import Flask
#importanto o SQL
from flask_sqlalchemy import SQLAlchemy

#chamando o flask
app = Flask(__name__)

#chamando o SQL e falando qual banco de dados vamos usar
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///dados.db'

#apresentando banco de dados
db = SQLAlchemy()
#esse conecta o banco de dados com a nossa aplicacao
db.init_app(app)


#criando classe
class Usuario(db.Model):
    #o nome da tabela
    _tablename_ = 'usuarios'
    #identificando o registro, Integer = inteiro(para numerico)
    #String(texto), (maximo de caracteres)
    #nullable(pode estar vazio), False = nao
    #unique = para ser unico
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False, unique=True)


@app.route('/')
def index():
    return "Olá, Mundo!"

if __name__ == '__main__':
    #para criar a instancia
    with app.app_context():
        db.create_all()
    app.run(debug=True)