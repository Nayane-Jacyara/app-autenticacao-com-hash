import pytest
from app import app, db
from app.models import Usuario  # Ajuste conforme a estrutura do seu código

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def init_db():
    db.create_all()  # Cria as tabelas no banco
    yield db
    db.drop_all()  # Remove as tabelas após o teste

def test_login(client, init_db):
    response = client.post('/login', data={
        'nome': 'usuario_teste', 
        'senha': 'senha_teste'
    })
    assert response.status_code == 200
