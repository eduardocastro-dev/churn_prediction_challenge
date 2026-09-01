# ==============================================================
# Dockerfile - Churn Prediction API
# Baseado no material da Aula 06 (Implantação de APIs: Container e Cloud)
# Adaptado à estrutura real do projeto (src/ + models/)
# ==============================================================

# Imagem base: Python 3.11 slim (menor e mais segura)
FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências primeiro (aproveita cache do Docker)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da API
COPY src/ ./src/

# Copia o modelo treinado
COPY models/ ./models/

# Expõe a porta que a API usa
EXPOSE 8000

# Comando para iniciar a API (src/api.py -> objeto "app")
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
