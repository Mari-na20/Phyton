from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    mensagem = "Olá, Mundo!"
    return render_template('myweb.html', mensagem=mensagem)


app.run(debug=True)