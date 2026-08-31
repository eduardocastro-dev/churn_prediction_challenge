from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# Variáveis numéricas utilizadas pelo modelo.
# As demais variáveis recebidas pelo pipeline são tratadas como categóricas.
COLUNAS_NUMERICAS = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
]


def criar_preprocessador(colunas):
    """
    Cria o pré-processador utilizado pelo modelo de churn.

    As variáveis numéricas são padronizadas com StandardScaler.
    As variáveis categóricas são transformadas com OneHotEncoder.
    """

    # Identifica as variáveis categóricas a partir das colunas disponíveis,
    # mantendo a mesma lógica utilizada durante o treinamento do modelo.
    colunas_categoricas = [
        coluna
        for coluna in colunas
        if coluna not in COLUNAS_NUMERICAS
    ]

    # Aplica transformações específicas para as variáveis numéricas
    # e categóricas dentro do mesmo pré-processador.
    preprocessador = ColumnTransformer(
        [
            (
                "num",
                StandardScaler(),
                COLUNAS_NUMERICAS,
            ),
            (
                "cat",
                OneHotEncoder(
                    handle_unknown="ignore",
                    drop="if_binary",
                ),
                colunas_categoricas,
            ),
        ]
    )

    return preprocessador
