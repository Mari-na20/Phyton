# Importar
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Conteúdo da página
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades Dinâmicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    if button_python:
        return render_template('index.html', button_python=button_python)

    button_html = request.form.get('button_html')
    if button_html:
        return render_template('index.html', button_html=button_html)
    
    button_discord = request.form.get('button_discord')
    if button_discord:
        return render_template('index.html', button_discord=button_discord)
    
    button_db = request.form.get('button_db')
    if button_db:
        return render_template('index.html', button_db=button_db)




if __name__ == "__main__":
    app.run(debug=True)
