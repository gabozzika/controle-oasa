from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estoque.db'  # Banco de dados SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definir o modelo para as solicitações
class Solicitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Pendente')

# Criar o banco de dados
with app.app_context():
    db.create_all()

# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de login
        return redirect(url_for('user_dashboard'))
    return render_template('login.html')

# Rota de Cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Lógica de cadastro
        return redirect(url_for('login'))
    return render_template('cadastro.html')

# Rota do Dashboard do Usuário
@app.route('/dashboard', methods=['GET', 'POST'])
def user_dashboard():
    if request.method == 'POST':
        item = request.form['item']
        nova_solicitacao = Solicitation(item=item)
        db.session.add(nova_solicitacao)
        db.session.commit()
        return redirect(url_for('user_dashboard'))

    solicitacoes = Solicitation.query.all()
    return render_template('user_dashboard.html', solicitacoes=solicitacoes)

# Rota do Dashboard do Administrador
@app.route('/admin_dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    if request.method == 'POST':
        id_solicitacao = request.form['id_solicitacao']
        solicitacao = Solicitation.query.get(id_solicitacao)
        solicitacao.status = 'Aprovado'
        db.session.commit()

    solicitacoes = Solicitation.query.all()
    return render_template('admin_dashboard.html', solicitacoes=solicitacoes)

if __name__ == '__main__':
    app.run(debug=True)
