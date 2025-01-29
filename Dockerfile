# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos da aplicação para o contêiner
COPY . /app

# Instalar as dependências
RUN pip install -r requirements.txt

# Expôr a porta da aplicação
EXPOSE 5000

# Definir o comando para iniciar a aplicação
CMD ["python", "app.py"]
