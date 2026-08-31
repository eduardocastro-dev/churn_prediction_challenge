from src.predict import prever_churn


# Cliente conhecido cuja probabilidade prevista pelo modelo é inferior
# ao threshold de 0,40.
CLIENTE_SEM_CHURN = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "Yes",
    "tenure": 59,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "Yes",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Two year",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Credit card (automatic)",
    "MonthlyCharges": 75.95,
    "TotalCharges": 4542.35,
}


# Cliente conhecido cuja probabilidade prevista pelo modelo é superior
# ao threshold de 0,40.
CLIENTE_COM_CHURN = {
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


def test_prever_cliente_sem_churn():
    """
    Verifica a classificação de um cliente conhecido cuja probabilidade
    prevista está abaixo do threshold definido para o modelo.
    """

    resultado = prever_churn(CLIENTE_SEM_CHURN)

    assert resultado["churn"] == 0
    assert resultado["threshold"] == 0.40
    assert 0.0 <= resultado["probabilidade"] <= 1.0


def test_prever_cliente_com_churn():
    """
    Verifica a classificação de um cliente conhecido cuja probabilidade
    prevista está acima do threshold definido para o modelo.
    """

    resultado = prever_churn(CLIENTE_COM_CHURN)

    assert resultado["churn"] == 1
    assert resultado["threshold"] == 0.40
    assert 0.0 <= resultado["probabilidade"] <= 1.0