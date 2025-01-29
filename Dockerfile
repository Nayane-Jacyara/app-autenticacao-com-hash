# Usando uma imagem base do Python
FROM python:3.9-slim

# Configurar o diretório de trabalho
WORKDIR /app

# Instalar as dependências diretamente no Dockerfile
RUN pip install --no-cache-dir Flask==2.2.3 \
    Flask-SQLAlchemy==3.0.2 \
    Flask-Bcrypt==1.0.1 \
    Flask-WTF==1.0.1

# Copiar o código da aplicação para dentro do container
COPY . /app/

# Expor a porta em que a aplicação irá rodar
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["python", "app.py"]
