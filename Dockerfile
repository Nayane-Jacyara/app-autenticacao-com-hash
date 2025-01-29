# Usando uma imagem base oficial do Python
FROM python:3.11-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos da aplicação para dentro do container
COPY . /app

# Atualizar o pip e instalar as dependências diretamente no Dockerfile
RUN pip install --upgrade pip && \
    pip install Flask Flask-SQLAlchemy Flask-Bcrypt Flask-WTF Flask-Admin pytest

# Expor a porta que o Flask vai rodar
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
