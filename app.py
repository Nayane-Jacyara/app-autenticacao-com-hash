from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Inicializando o Flask e o banco de dados
app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta_segura'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Modelo de Usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    senha = db.Column(db.String(60), nullable=False)

# Configurar o Flask-Admin
admin = Admin(app, name='Admin', template_mode='123456')
admin.add_view(ModelView(Usuario, db.session))

# Formulário de Cadastro
class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=150)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField('Cadastrar')

    def validate_nome(self, nome):
        usuario = Usuario.query.filter_by(nome=nome.data).first()
        if usuario:
            raise ValidationError('Esse nome já está em uso. Por favor, escolha outro.')

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('home.html')

# Rota para Cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        senha_hash = bcrypt.generate_password_hash(form.senha.data).decode('utf-8')
        novo_usuario = Usuario(nome=form.nome.data, senha=senha_hash)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))
    return render_template('cadastro.html', form=form)

# Formulário de Login
class LoginForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

# Rota para Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(nome=form.nome.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form.senha.data):
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Falha no login. Verifique o nome e a senha.', 'danger')
    return render_template('login.html', form=form)

# Rota para o dashboard (após login)
@app.route('/dashboard')
def dashboard():
    return 'Você está logado!'

# Rota para listar usuários (temporária para desenvolvimento)
@app.route('/usuarios')
def lista_usuarios():
    usuarios = Usuario.query.all()
    return '<br>'.join([f'ID: {u.id}, Nome: {u.nome}' for u in usuarios])

# Criar o banco de dados e as tabelas
with app.app_context():
    db.create_all()

# Inicializando a aplicação
if __name__ == '__main__':
    app.run(debug=True)
