from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 🔐 chave da sessão
app.secret_key = 'my_top_secret_123'

# 🗄️ banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------------
# TABELA DE CARDS
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
# TABELA DE USUÁRIOS
# -------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

# -------------------------
# LOGIN
# -------------------------
@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''

    if request.method == 'POST':
        form_login = request.form['email']
        form_password = request.form['password']

        # 🔎 busca usuário no banco
        user = User.query.filter_by(email=form_login, password=form_password).first()

        if user:
            session['user_email'] = user.email
            return redirect('/index')
        else:
            error = "Email ou senha incorretos"

    return render_template('login.html', error=error)

# -------------------------
# REGISTRO
# -------------------------
@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # 🚫 evita email duplicado
        user_existente = User.query.filter_by(email=email).first()

        if user_existente:
            return "Este email já está cadastrado!"

        user = User(email=email, password=password)

        db.session.add(user)
        db.session.commit()

        return redirect('/')

    return render_template('registration.html')

# -------------------------
# PÁGINA PRINCIPAL
# -------------------------
@app.route('/index')
def index():

    if 'user_email' not in session:
        return redirect('/')

    email = session.get('user_email')

    cards = Card.query.filter_by(user_email=email).all()

    return render_template('index.html', cards=cards)

# -------------------------
# VER CARD
# -------------------------
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)
    return render_template('card.html', card=card)

# -------------------------
# PÁGINA DE CRIAÇÃO
# -------------------------
@app.route('/create')
def create():
    if 'user_email' not in session:
        return redirect('/')

    return render_template('create_card.html')

# -------------------------
# FORMULÁRIO DE CRIAÇÃO
# -------------------------
@app.route('/form_create', methods=['POST'])
def form_create():

    if 'user_email' not in session:
        return redirect('/')

    title = request.form['title']
    subtitle = request.form['subtitle']
    text = request.form['text']

    email = session.get('user_email')

    # ✅ agora com o nome correto
    card = Card(title=title, subtitle=subtitle, text=text, user_email=email)

    db.session.add(card)
    db.session.commit()

    return redirect('/index')

# -------------------------
# LOGOUT
# -------------------------
@app.route('/logout')
def logout():
    session.pop('user_email', None)
    return redirect('/')

# -------------------------
# EDITAR CARD (ABRIR PÁGINA)
# -------------------------
@app.route('/edit/<int:id>')
def edit(id):

    if 'user_email' not in session:
        return redirect('/')

    card = Card.query.get_or_404(id)

    # 🔒 garante que só o dono pode editar
    if card.user_email != session['user_email']:
        return "Você não tem permissão para editar este card!"

    return render_template('edit_card.html', card=card)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):

    if 'user_email' not in session:
        return redirect('/')

    card = Card.query.get_or_404(id)

    if card.user_email != session['user_email']:
        return "Você não tem permissão para editar este card!"

    card.title = request.form['title']
    card.subtitle = request.form['subtitle']
    card.text = request.form['text']

    db.session.commit()

    return redirect('/index')

# -------------------------
# INICIAR APP
# -------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)