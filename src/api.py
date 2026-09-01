from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from src.predict import prever_churn


# Cria a aplicação FastAPI responsável por disponibilizar
# o modelo de previsão de churn por meio de uma API HTTP.
app = FastAPI(
    title="Churn Prediction API",
    description="API para previsão de churn de clientes.",
    version="1.0.0",
)


class DadosCliente(BaseModel):
    """
    Define e valida os dados de entrada esperados pelo modelo
    para realizar uma previsão de churn.
    """

    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/", include_in_schema=False)
def raiz():
    """
    Redireciona a raiz da aplicação para a documentação interativa,
    já que não há um endpoint funcional definido para "/".
    """
    return RedirectResponse(url="/docs")

@app.get("/health")
def verificar_saude():
    """
    Endpoint utilizado para verificar se a API está disponível
    e respondendo corretamente.
    """

    return {
        "status": "ok"
    }


@app.post("/predict")
def prever(dados_cliente: DadosCliente):
    """
    Recebe os dados de um cliente, executa o modelo de churn
    e retorna a classificação, a probabilidade e o threshold utilizado.
    """

    return prever_churn(dados_cliente.model_dump())