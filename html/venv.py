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

@app.route('/image')
def image_world():
    return '<img src = "https://tse1.mm.bing.net/th/id/OIP.Pf7QR3jLcqlZF0DjAKWUQQHaE7?rs=1&pid=ImgDetMain&o=7&rm=3" width="300" height="250" alt="Descrição da imagem" >'

@app.route('/things')
def out_world():
    return ''' <h1> Pokemons!!! <h1> 
    <p> Esse e o Pikachu: <p>
    <img src="https://th.bing.com/th/id/R.42ccd03330ac246a64c64bf83c92e85c?rik=0M6mOCiPFioR8w&riu=http%3a%2f%2fwww.pixelstalk.net%2fwp-content%2fuploads%2f2016%2f03%2fPokemon-pikachu-hd-wallpaper-background.jpg&ehk=57em4wEyX828IbSz8M6zk945VMOybDtXV209W5Z6RwU%3d&risl=&pid=ImgRaw&r=0" width="300" height="250" alt="Descrição da imagem">

    '''


app.run(debug=True)
