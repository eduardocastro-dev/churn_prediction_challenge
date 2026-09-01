from typing import Literal

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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

    gender: Literal["Female", "Male"]
    SeniorCitizen: Literal[0, 1]
    Partner: Literal["No", "Yes"]
    Dependents: Literal["No", "Yes"]
    tenure: int
    PhoneService: Literal["No", "Yes"]
    MultipleLines: Literal["No", "No phone service", "Yes"]
    InternetService: Literal["DSL", "Fiber optic", "No"]
    OnlineSecurity: Literal["No", "No internet service", "Yes"]
    OnlineBackup: Literal["No", "No internet service", "Yes"]
    DeviceProtection: Literal["No", "No internet service", "Yes"]
    TechSupport: Literal["No", "No internet service", "Yes"]
    StreamingTV: Literal["No", "No internet service", "Yes"]
    StreamingMovies: Literal["No", "No internet service", "Yes"]
    Contract: Literal["Month-to-month", "One year", "Two year"]
    PaperlessBilling: Literal["No", "Yes"]
    PaymentMethod: Literal[
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check",
    ]
    MonthlyCharges: float
    TotalCharges: float


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def raiz():
    """
    Disponibiliza uma interface simples para preenchimento dos dados
    do cliente e realização da previsão de churn.
    """

    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Churn Prediction</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                padding: 40px 20px;
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                color: #1f2937;
            }

            .container {
                max-width: 1000px;
                margin: 0 auto;
                background: white;
                padding: 32px;
                border-radius: 12px;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
            }

            h1 {
                margin-top: 0;
                margin-bottom: 8px;
            }

            .descricao {
                margin-top: 0;
                margin-bottom: 30px;
                color: #6b7280;
            }

            .formulario {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 20px;
            }

            .campo {
                display: flex;
                flex-direction: column;
            }

            label {
                font-weight: 600;
                margin-bottom: 6px;
            }

            select,
            input {
                width: 100%;
                padding: 10px 12px;
                border: 1px solid #d1d5db;
                border-radius: 6px;
                background: white;
                font-size: 14px;
            }

            select:focus,
            input:focus {
                outline: none;
                border-color: #2563eb;
            }

            .acoes {
                margin-top: 28px;
            }

            button {
                border: 0;
                border-radius: 6px;
                padding: 12px 24px;
                background: #2563eb;
                color: white;
                font-size: 15px;
                font-weight: 600;
                cursor: pointer;
            }

            button:hover {
                background: #1d4ed8;
            }

            button:disabled {
                opacity: 0.6;
                cursor: wait;
            }

            #resultado {
                display: none;
                margin-top: 30px;
                padding: 20px;
                border-radius: 8px;
                background: #f9fafb;
                border: 1px solid #e5e7eb;
            }

            #resultado h2 {
                margin-top: 0;
            }

            .resultado-linha {
                margin: 8px 0;
            }

            .valor {
                font-weight: 700;
            }

            .churn {
                color: #b91c1c;
            }

            .sem-churn {
                color: #047857;
            }

            .erro {
                color: #b91c1c;
            }

            .links {
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #e5e7eb;
                font-size: 14px;
            }

            .links a {
                color: #2563eb;
                text-decoration: none;
                margin-right: 20px;
            }

            @media (max-width: 700px) {
                .formulario {
                    grid-template-columns: 1fr;
                }

                body {
                    padding: 20px 10px;
                }

                .container {
                    padding: 20px;
                }
            }
        </style>
    </head>

    <body>
        <div class="container">

            <h1>Predição de Churn</h1>

            <p class="descricao">
                Informe os dados do cliente para estimar a probabilidade de churn.
            </p>

            <form id="formulario">

                <div class="formulario">

                    <div class="campo">
                        <label for="gender">Gender</label>
                        <select id="gender">
                            <option value="Female">Female</option>
                            <option value="Male">Male</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="SeniorCitizen">Senior Citizen</label>
                        <select id="SeniorCitizen">
                            <option value="0">No</option>
                            <option value="1">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="Partner">Partner</label>
                        <select id="Partner">
                            <option value="No">No</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="Dependents">Dependents</label>
                        <select id="Dependents">
                            <option value="No">No</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="tenure">Tenure (months)</label>
                        <input
                            id="tenure"
                            type="number"
                            min="0"
                            step="1"
                            value="12"
                            required
                        >
                    </div>

                    <div class="campo">
                        <label for="PhoneService">Phone Service</label>
                        <select id="PhoneService">
                            <option value="No">No</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="MultipleLines">Multiple Lines</label>
                        <select id="MultipleLines">
                            <option value="No">No</option>
                            <option value="No phone service">No phone service</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="InternetService">Internet Service</label>
                        <select id="InternetService">
                            <option value="DSL">DSL</option>
                            <option value="Fiber optic">Fiber optic</option>
                            <option value="No">No</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="OnlineSecurity">Online Security</label>
                        <select id="OnlineSecurity">
                            <option value="No">No</option>
                            <option value="No internet service">No internet service</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="OnlineBackup">Online Backup</label>
                        <select id="OnlineBackup">
                            <option value="No">No</option>
                            <option value="No internet service">No internet service</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="DeviceProtection">Device Protection</label>
                        <select id="DeviceProtection">
                            <option value="No">No</option>
                            <option value="No internet service">No internet service</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="TechSupport">Tech Support</label>
                        <select id="TechSupport">
                            <option value="No">No</option>
                            <option value="No internet service">No internet service</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="StreamingTV">Streaming TV</label>
                        <select id="StreamingTV">
                            <option value="No">No</option>
                            <option value="No internet service">No internet service</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="StreamingMovies">Streaming Movies</label>
                        <select id="StreamingMovies">
                            <option value="No">No</option>
                            <option value="No internet service">No internet service</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="Contract">Contract</label>
                        <select id="Contract">
                            <option value="Month-to-month">Month-to-month</option>
                            <option value="One year">One year</option>
                            <option value="Two year">Two year</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="PaperlessBilling">Paperless Billing</label>
                        <select id="PaperlessBilling">
                            <option value="No">No</option>
                            <option value="Yes">Yes</option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="PaymentMethod">Payment Method</label>
                        <select id="PaymentMethod">
                            <option value="Bank transfer (automatic)">
                                Bank transfer (automatic)
                            </option>
                            <option value="Credit card (automatic)">
                                Credit card (automatic)
                            </option>
                            <option value="Electronic check">
                                Electronic check
                            </option>
                            <option value="Mailed check">
                                Mailed check
                            </option>
                        </select>
                    </div>

                    <div class="campo">
                        <label for="MonthlyCharges">Monthly Charges</label>
                        <input
                            id="MonthlyCharges"
                            type="number"
                            min="0"
                            step="0.01"
                            value="70.00"
                            required
                        >
                    </div>

                    <div class="campo">
                        <label for="TotalCharges">Total Charges</label>
                        <input
                            id="TotalCharges"
                            type="number"
                            min="0"
                            step="0.01"
                            value="840.00"
                            required
                        >
                    </div>

                </div>

                <div class="acoes">
                    <button id="botaoPrever" type="submit">
                        Prever churn
                    </button>
                </div>

            </form>

            <div id="resultado"></div>

            <div class="links">
                <a href="/docs">Documentação da API</a>
                <a href="/health">Health check</a>
            </div>

        </div>

        <script>
            const formulario = document.getElementById("formulario");
            const resultado = document.getElementById("resultado");
            const botaoPrever = document.getElementById("botaoPrever");

            formulario.addEventListener("submit", async function (evento) {
                evento.preventDefault();

                botaoPrever.disabled = true;
                botaoPrever.textContent = "Calculando...";

                resultado.style.display = "none";

                const dadosCliente = {
                    gender: document.getElementById("gender").value,
                    SeniorCitizen: Number(
                        document.getElementById("SeniorCitizen").value
                    ),
                    Partner: document.getElementById("Partner").value,
                    Dependents: document.getElementById("Dependents").value,
                    tenure: Number(
                        document.getElementById("tenure").value
                    ),
                    PhoneService: document.getElementById("PhoneService").value,
                    MultipleLines: document.getElementById("MultipleLines").value,
                    InternetService: document.getElementById("InternetService").value,
                    OnlineSecurity: document.getElementById("OnlineSecurity").value,
                    OnlineBackup: document.getElementById("OnlineBackup").value,
                    DeviceProtection: document.getElementById("DeviceProtection").value,
                    TechSupport: document.getElementById("TechSupport").value,
                    StreamingTV: document.getElementById("StreamingTV").value,
                    StreamingMovies: document.getElementById("StreamingMovies").value,
                    Contract: document.getElementById("Contract").value,
                    PaperlessBilling: document.getElementById("PaperlessBilling").value,
                    PaymentMethod: document.getElementById("PaymentMethod").value,
                    MonthlyCharges: Number(
                        document.getElementById("MonthlyCharges").value
                    ),
                    TotalCharges: Number(
                        document.getElementById("TotalCharges").value
                    )
                };

                try {
                    const resposta = await fetch("/predict", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify(dadosCliente)
                    });

                    if (!resposta.ok) {
                        const detalhe = await resposta.text();

                        throw new Error(
                            "A API retornou o status " +
                            resposta.status +
                            ": " +
                            detalhe
                        );
                    }

                    const previsao = await resposta.json();

                    const probabilidade =
                        (previsao.probabilidade * 100).toFixed(2);

                    const threshold =
                        (previsao.threshold * 100).toFixed(0);

                    const classificacao =
                        previsao.churn === 1
                            ? "CHURN"
                            : "SEM CHURN";

                    const classeResultado =
                        previsao.churn === 1
                            ? "churn"
                            : "sem-churn";

                    resultado.innerHTML = `
                        <h2>Resultado</h2>

                        <div class="resultado-linha">
                            Classificação:
                            <span class="valor ${classeResultado}">
                                ${classificacao}
                            </span>
                        </div>

                        <div class="resultado-linha">
                            Probabilidade de churn:
                            <span class="valor">
                                ${probabilidade}%
                            </span>
                        </div>

                        <div class="resultado-linha">
                            Threshold:
                            <span class="valor">
                                ${threshold}%
                            </span>
                        </div>
                    `;

                    resultado.style.display = "block";

                } catch (erro) {
                    resultado.innerHTML = `
                        <h2>Erro</h2>
                        <div class="erro">
                            Não foi possível realizar a previsão.
                        </div>
                    `;

                    resultado.style.display = "block";

                    console.error(erro);

                } finally {
                    botaoPrever.disabled = false;
                    botaoPrever.textContent = "Prever churn";
                }
            });
        </script>

    </body>
    </html>
    """


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