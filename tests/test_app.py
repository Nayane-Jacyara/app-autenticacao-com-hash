import sys
import os
from app import app, db
import pytest

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def client():
    # Cria uma instância do cliente de testes do Flask
    with app.test_client() as client:
        # Garante que as tabelas do banco de dados sejam criadas
        with app.app_context():
            db.create_all()
        yield client
        # Após o teste, limpa os dados do banco de dados
        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_home(client):
    # Testa a página inicial
    response = client.get('/')
    assert response.status_code == 200
    assert b'Home' in response.data  # Verifica se a palavra "Home" está na página

def test_cadastro(client):
    # Testa o cadastro de um usuário
    response = client.post('/cadastro', data={
        'nome': 'Teste',
        'senha': 'senha123',
        'confirmar_senha': 'senha123'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Cadastro realizado com sucesso!' in response.data

def test_login(client):
    # Testa o login de um usuário
    # Primeiro, cria um usuário
    with app.app_context():
        user = Usuario(nome='Teste', senha='senha123')
        db.session.add(user)
        db.session.commit()
    
    # Tenta fazer login com o usuário
    response = client.post('/login', data={
        'nome': 'Teste',
        'senha': 'senha123'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Login realizado com sucesso!' in response.data

def test_lista_usuarios(client):
    # Testa a listagem de usuários
    response = client.get('/usuarios')
    assert response.status_code == 200
    assert b'Lista de Usuários' in response.data
