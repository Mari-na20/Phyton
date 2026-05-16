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
    __tablename__ = 'usuarios'
    #identificando o registro, Integer = inteiro(para numerico)
    #String(texto), (maximo de caracteres)
    #nullable(pode estar vazio), False = nao
    #unique = para ser unico
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False, unique=True)

    def __repr__ (self):
        return f"<{self.nome}>"


@app.route('/')
def index():
    return "Olá, Mundo!"

if __name__ == '__main__':
    #para criar a instancia ->
    #usa so uma vez (quando inicia a pagina), depois apaga
    with app.app_context():
        db.create_all()

        #para criar algo na tabela:
        #user = Usuario(nome="Estela")
        #db.session.add(user)
        #db.session.commit()

        #obter dados do banco de dados, query = pedido, Usuario = classe, all = tudo
        usuarios = db.session.query(Usuario).all()

        #para imprimir um registro especifico
        #user = db.session.query(Usuario).filter_by(id = 2).first()
        #para mudar de nome:
        #user.nome = "Julia" - se for para deletar: db.session.delete(user)
        #db.session.commit()

        #para escrever a lista:
        #for us in usuarios:
            #print(f"Usuario:{us.nome}")

        print(usuarios)
    app.run(debug=True)