from fastapi.testclient import TestClient

from src.api import app


# Cria um cliente de teste que permite fazer requisições para a API
# diretamente pelo pytest, sem precisar iniciar o servidor Uvicorn.
cliente_api = TestClient(app)


def test_health():
    """
    Verifica se o endpoint de saúde da API está disponível
    e retorna o status esperado.
    """

    resposta = cliente_api.get("/health")

    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}


def test_predict():
    """
    Verifica se o endpoint de predição recebe os dados de um cliente
    e retorna corretamente a classificação de churn.
    """

    dados_cliente = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 1,
        "PhoneService": "No",
        "MultipleLines": "No phone service",
        "InternetService": "DSL",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 29.85,
        "TotalCharges": 29.85,
    }

    resposta = cliente_api.post(
        "/predict",
        json=dados_cliente,
    )

    resultado = resposta.json()

    assert resposta.status_code == 200
    assert resultado["churn"] == 1
    assert resultado["threshold"] == 0.40
    assert 0.0 <= resultado["probabilidade"] <= 1.0