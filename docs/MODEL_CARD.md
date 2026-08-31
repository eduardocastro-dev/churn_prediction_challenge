# Model Card — Predição de Churn

## 1. Visão geral

Este modelo foi desenvolvido para prever a probabilidade de churn de clientes de uma empresa de telecomunicações.

O objetivo é identificar clientes com maior probabilidade de cancelamento, permitindo que a empresa direcione ações de retenção de forma mais eficiente.

O problema foi tratado como uma classificação binária:

- 0: cliente sem churn
- 1: cliente com churn

O modelo retorna tanto a classificação prevista quanto a probabilidade estimada de churn.

## 2. Modelo selecionado

O modelo final selecionado foi uma Regressão Logística, utilizando um threshold de classificação de 0,40.

A escolha foi realizada após a comparação com modelos de maior complexidade, incluindo Random Forest e MLPClassifier, além de diferentes estratégias de ajuste do baseline.

A Regressão Logística com threshold de 0,40 apresentou o melhor F1-score entre as alternativas avaliadas, mantendo bom desempenho de ROC-AUC e aumentando a capacidade de identificação dos clientes que efetivamente apresentaram churn.

## 3. Dados utilizados

O desenvolvimento utilizou o conjunto de dados IBM Telco Customer Churn, composto originalmente por 7.043 registros de clientes e 21 variáveis.

A variável `customerID` foi removida por representar apenas um identificador do cliente, sem significado preditivo para o problema.

A variável alvo utilizada foi `Churn`, convertida para representação binária:

- No = 0
- Yes = 1

Durante a preparação dos dados, foram identificados 11 registros sem valor válido em `TotalCharges`. Esses registros correspondiam a clientes com `tenure` igual a zero e foram removidos da base utilizada para modelagem.

Após o tratamento, foram utilizados 7.032 registros.

Os dados foram divididos em conjuntos de treinamento e teste na proporção de 80% e 20%, respectivamente, utilizando divisão estratificada pela variável alvo e `random_state=42`.

## 4. Pré-processamento

O pré-processamento foi implementado utilizando um `ColumnTransformer`, permitindo aplicar tratamentos diferentes às variáveis numéricas e categóricas.

As variáveis numéricas utilizadas foram:

- `tenure`
- `MonthlyCharges`
- `TotalCharges`

Essas variáveis foram padronizadas utilizando `StandardScaler`.

As demais variáveis preditoras foram tratadas como categóricas e transformadas utilizando `OneHotEncoder`, configurado com `handle_unknown="ignore"` e `drop="if_binary"`.

O pré-processamento e o classificador são integrados por meio de um `Pipeline` do scikit-learn, garantindo que as mesmas transformações utilizadas durante o treinamento sejam aplicadas durante a realização das previsões.

## 5. Avaliação do modelo

O desempenho dos modelos foi avaliado principalmente pelo F1-score, por representar um equilíbrio entre precision e recall em um problema com distribuição desigual entre as classes.

O ROC-AUC foi utilizado como métrica complementar para avaliar a capacidade geral dos modelos de distinguir clientes com e sem churn. Precision e recall também foram considerados na análise.

Foram avaliadas diferentes abordagens, incluindo:

- Regressão Logística utilizada como baseline
- Regressão Logística com engenharia de features
- Regressão Logística com balanceamento de classes
- Regressão Logística com diferentes thresholds de classificação
- Random Forest
- Random Forest com ajuste de hiperparâmetros
- MLPClassifier
- MLPClassifier com ajuste de hiperparâmetros

O modelo selecionado apresentou, no conjunto de teste:

| Métrica | Resultado aproximado |

| F1-score  | 0,629 |
| ROC-AUC   | 0,836 |
| Precision | 0,582 |
| Recall    | 0,684 |
| Threshold | 0,40  |

## 6. Escolha do threshold

O threshold padrão de 0,50 utilizado em classificadores binários foi comparado com outros valores.

A utilização de um threshold de 0,40 aumentou o recall do modelo e resultou em F1-score superior ao obtido com o threshold padrão.

No contexto de churn, esse comportamento é relevante porque aumenta a capacidade de identificar clientes que apresentam risco de cancelamento, ainda que isso também possa aumentar a quantidade de falsos positivos.

Por esse motivo, o threshold de 0,40 foi adotado para a classificação final.

O modelo persistido gera as probabilidades de churn por meio de `predict_proba`. O threshold de 0,40 é aplicado posteriormente pela lógica de predição disponível em `src/predict.py`.

## 7. Uso pretendido

O modelo foi desenvolvido como uma solução de apoio à identificação de clientes com maior probabilidade de churn.

A previsão pode ser utilizada para priorizar clientes em ações de retenção, permitindo que equipes responsáveis concentrem esforços nos casos classificados com maior risco de cancelamento.

O resultado do modelo deve ser interpretado como um indicador de risco e não como uma certeza de que determinado cliente irá cancelar o serviço.

## 8. Limitações e riscos

O modelo foi desenvolvido e avaliado utilizando o conjunto de dados IBM Telco Customer Churn. Dessa forma, seu desempenho foi medido sobre dados com as características e distribuições presentes nessa base.

A utilização do modelo em dados de outra empresa ou em uma população com características diferentes pode resultar em desempenho distinto do observado durante o desenvolvimento.

O threshold de 0,40 aumenta a capacidade de identificação de clientes com churn, mas também pode aumentar a quantidade de falsos positivos. Consequentemente, alguns clientes podem ser classificados como risco de churn mesmo sem efetivamente cancelar o serviço.

Além disso, mudanças no comportamento dos clientes ao longo do tempo podem alterar a relação entre as variáveis e o churn. Em uma aplicação real, o desempenho do modelo deve ser monitorado periodicamente e o modelo deve ser reavaliado ou retreinado quando necessário.

## 9. Considerações sobre a avaliação

A seleção do modelo e do threshold foi realizada a partir dos resultados obtidos durante o desenvolvimento do projeto.

O threshold de 0,40 foi avaliado utilizando o conjunto de teste. Em um cenário de produção, seria recomendável utilizar um conjunto de validação independente ou validação cruzada para selecionar esse parâmetro, preservando o conjunto de teste exclusivamente para a avaliação final.

Essa característica deve ser considerada ao interpretar as métricas reportadas neste projeto.

## 10. Artefatos relacionados

Os principais artefatos associados ao modelo são:

- `models/churn_model.joblib`: pipeline treinado e persistido.
- `src/preprocessing.py`: definição do pré-processamento utilizado no treinamento.
- `src/predict.py`: carregamento do modelo e aplicação do threshold de classificação.
- `src/api.py`: API FastAPI para disponibilização das previsões.
- `tests/`: testes automatizados da solução.
- `notebooks/01_eda_normalizacao.ipynb`: análise exploratória, preparação dos dados e desenvolvimento do baseline.
- `notebooks/02_comparacao_de_modelos.ipynb`: comparação dos modelos e seleção da solução final.