from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    comentario = db.Column(db.Text, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        comentario = request.form.get('text')

        if email and comentario:
            novo = Feedback(email=email, comentario=comentario)
            db.session.add(novo)
            db.session.commit()

    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)