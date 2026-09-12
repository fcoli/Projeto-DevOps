FROM python:3.12-slim

# Cria um usuario nao-root para rodar a aplicacao (boa pratica de seguranca)
RUN useradd --create-home appuser

WORKDIR /app

# Copia e instala as dependencias primeiro (aproveita o cache de camadas do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o codigo da aplicacao
COPY app.py .

# Garante que o usuario appuser tem acesso ao diretorio da aplicacao
RUN chown -R appuser:appuser /app
USER appuser

ENTRYPOINT ["python", "app.py"]
