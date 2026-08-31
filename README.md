# Churn Prediction Challenge

Projeto desenvolvido para o Tech Challenge de Machine Learning Engineering da FIAP.

O objetivo é desenvolver uma solução de Machine Learning capaz de identificar clientes com maior probabilidade de churn, passando pelas etapas de análise exploratória, preparação dos dados, treinamento e comparação de modelos, disponibilização do modelo por API e criação de testes automatizados.

## Modelo final

Após a avaliação das alternativas desenvolvidas, o modelo selecionado foi uma Regressão Logística com threshold de classificação ajustado para 0,40.

Principais resultados obtidos no conjunto de teste:

| Métrica | Resultado aproximado |

| F1-score  | 0,629 |
| ROC-AUC   | 0,836 |
| Precision | 0,582 |
| Recall    | 0,684 |

O threshold de 0,40 foi escolhido para aumentar a capacidade de identificação de clientes com churn, priorizando maior recall sem perder o equilíbrio representado pelo F1-score.

## Estrutura do projeto

```text
churn_prediction_challenge/
├── data/
├── docs/
│   ├── ML_CANVAS.md
│   └── MODEL_CARD.md
├── models/
│   └── churn_model.joblib
├── notebooks/
│   ├── 01_eda_normalizacao.ipynb
│   └── 02_comparacao_de_modelos.ipynb
├── src/
│   ├── api.py
│   ├── predict.py
│   └── preprocessing.py
├── tests/
│   ├── test_api.py
│   └── test_predict.py
├── .gitignore
├── README.md
└── requirements.txt

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/rafacferreira/churn_prediction_challenge.git
cd churn_prediction_challenge
```

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

No Windows PowerShell, ative o ambiente com:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

## Execução dos testes

Com o ambiente virtual ativado, execute:

```bash
python -m pytest tests -v
```

Os testes verificam o funcionamento da lógica de predição e dos endpoints disponibilizados pela API.

## Execução da API

Para iniciar a API localmente:

```bash
python -m uvicorn src.api:app --reload
```

Por padrão, a aplicação ficará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa gerada automaticamente pelo FastAPI pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### GET /health

Verifica se a API está disponível.

Resposta esperada:

```json
{
  "status": "ok"
}
```

### POST /predict

Recebe os dados de um cliente e retorna a previsão de churn, a probabilidade estimada e o threshold utilizado.

Exemplo de resposta:

```json
{
  "churn": 1,
  "probabilidade": 0.623504389462201,
  "threshold": 0.4
}
```

## Tecnologias utilizadas

O projeto foi desenvolvido em Python e utiliza principalmente:

- pandas e NumPy para manipulação e análise dos dados
- Matplotlib e Seaborn para visualização
- scikit-learn para pré-processamento, treinamento e avaliação dos modelos
- imbalanced-learn para experimentos com balanceamento de classes
- joblib para persistência do modelo
- FastAPI e Uvicorn para disponibilização da API
- pytest para testes automatizados
- Jupyter Notebook para análise exploratória e experimentação

As versões utilizadas estão especificadas no arquivo `requirements.txt`.

## Reprodução da análise

A análise e a modelagem estão organizadas em dois notebooks.

### 1. Análise exploratória e baseline

```text
notebooks/01_eda_normalizacao.ipynb
```

Contém a exploração dos dados, tratamento das variáveis, definição do pré-processamento e desenvolvimento do modelo baseline.

### 2. Comparação e seleção dos modelos

```text
notebooks/02_comparacao_de_modelos.ipynb
```

Contém os experimentos com diferentes abordagens de modelagem, validação cruzada, ajustes de hiperparâmetros, comparação das métricas e seleção do modelo final.

## Documentação do projeto

O contexto de negócio, stakeholders, métricas de negócio e critérios de sucesso da solução estão documentados em:

`docs/ML_CANVAS.md`

Informações detalhadas sobre o modelo selecionado, dados utilizados, pré-processamento, métricas, uso pretendido, riscos e limitações estão disponíveis em:

`docs/MODEL_CARD.md`

## Observações

O projeto utiliza o dataset IBM Telco Customer Churn e foi desenvolvido com finalidade acadêmica no contexto do Tech Challenge de Machine Learning Engineering da FIAP.

As métricas apresentadas correspondem ao conjunto de dados utilizado no desenvolvimento e não garantem o mesmo desempenho em dados externos ou em um ambiente real de produção.