# Importações
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# Chave secreta para uso de session
app.secret_key = 'my_top_secret_123'
# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Inicializando o banco
db = SQLAlchemy(app)
# -------------------------
# Tabela de Cards
# -------------------------
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return f'<Card {self.id}>'

# -------------------------
# Atividade #1
# Criar a tabela User
# -------------------------


# -------------------------
# Login
# -------------------------
@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']
        # Atividade #4. Verificação do usuário
        
    return render_template('login.html')

# -------------------------
# # Registro
# -------------------------
@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Atividade #3. Salvar usuário no banco
        
        return redirect('/')
    return render_template('registration.html')

# -------------------------
# Página principal
# -------------------------
@app.route('/index')
def index():
    # Atividade #4. Mostrar apenas os cards do usuário logado
    
    return render_template('index.html', cards=cards)

# -------------------------
# Página do card
# -------------------------
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)
    return render_template('card.html', card=card)

# -------------------------
# Criar card
# -------------------------
@app.route('/create')
def create():
    return render_template('create_card.html')

# -------------------------
# Formulário de criação
# -------------------------
@app.route('/form_create', methods=['GET', 'POST'])
def form_create():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        text = request.form['text']
        # Atividade #4. Criar card em nome do usuário logado
        
        return redirect('/index')
    return render_template('create_card.html')

if __name__ == "__main__":
    app.run(debug=True)