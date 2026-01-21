from flask import Flask
import random

app = Flask(__name__)

facts_list = 'Elon Musk também defende a regulamentação das redes sociais e a proteção dos dados pessoais dos usuários. Ele afirma que as redes sociais coletam uma enorme quantidade de informações sobre nós, que podem ser usadas para manipular nossos pensamentos e comportamentos',' De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones',' Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, fazendo com que passemos o máximo de tempo possível consumindo conteúdo',' A maioria das pessoas que sofre de dependência tecnológica sente um forte estresse quando fica fora da área de cobertura de rede ou não pode usar seus dispositivos'
moeda_list = 'Cara','Coroa'

@app.route("/")
def hello_world():
    return f'<h1>{random.choice(moeda_list)}</h1>'

@app.route('/secret')
def bye_world():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)
