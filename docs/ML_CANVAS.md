# ML Canvas — Predição de Churn

## 1. Problema de negócio

Empresas de telecomunicações enfrentam perdas de receita quando clientes cancelam seus serviços. Identificar antecipadamente clientes com maior probabilidade de churn permite direcionar ações de retenção antes que o cancelamento ocorra.

O problema de negócio deste projeto consiste em utilizar dados históricos dos clientes para estimar o risco de churn e apoiar a priorização de ações de retenção.

## 2. Objetivo da solução de Machine Learning

Desenvolver um modelo de classificação capaz de estimar a probabilidade de churn de cada cliente.

A solução deve permitir identificar clientes com maior risco de cancelamento e disponibilizar essa previsão de forma reutilizável por meio de uma API.

A saída do modelo é composta por:

- probabilidade estimada de churn;
- classificação do cliente como churn ou não churn;
- threshold utilizado para realizar a classificação.

## 3. Stakeholders

Os principais stakeholders considerados para a solução são:

- Equipe de Retenção: utiliza as previsões para priorizar clientes em ações de retenção.
- Marketing e Relacionamento: pode utilizar a identificação de risco para direcionar campanhas e ofertas.
- Gestão do negócio: acompanha o impacto das ações sobre churn, retenção e resultados financeiros.
- Equipe de Dados e Machine Learning: responsável pelo desenvolvimento, avaliação, disponibilização e monitoramento do modelo.

## 4. Métricas de negócio

O valor de negócio do modelo está relacionado à capacidade de direcionar ações de retenção para clientes com maior probabilidade de cancelamento.

Em uma aplicação real, o desempenho da solução pode ser acompanhado por indicadores como:

- taxa de churn;
- taxa de retenção entre clientes abordados;
- quantidade de clientes em risco identificados;
- custo das ações de retenção;
- receita preservada por clientes retidos.

Essas métricas permitem avaliar se a utilização das previsões produz impacto efetivo no negócio, além do desempenho estatístico do modelo.

## 5. Métricas técnicas

O F1-score foi definido como principal métrica técnica do projeto por equilibrar precision e recall, considerando a distribuição desigual entre clientes com e sem churn.

Como métricas complementares foram utilizadas:

- ROC-AUC: capacidade geral de discriminação entre as classes;
- Precision: proporção dos clientes classificados como churn que efetivamente apresentaram churn;
- Recall: proporção dos clientes com churn que foram identificados pelo modelo.

O modelo final selecionado apresentou aproximadamente:

| Métrica   | Resultado |

| F1-score  | 0,629 |
| ROC-AUC   | 0,836 |
| Precision | 0,582 |
| Recall    | 0,684 |

O threshold de classificação foi ajustado de 0,50 para 0,40, aumentando o recall e resultando no melhor F1-score entre as alternativas avaliadas.

## 6. Dados e variáveis

O projeto utiliza o conjunto de dados IBM Telco Customer Churn, contendo informações demográficas, características dos serviços contratados, informações de cobrança e histórico de permanência dos clientes.

A variável alvo é `Churn`, representando se o cliente cancelou ou não o serviço.

Entre as informações utilizadas pelo modelo estão:

- tempo de permanência do cliente (`tenure`);
- valor mensal (`MonthlyCharges`);
- valor total acumulado (`TotalCharges`);
- tipo de contrato;
- serviços contratados;
- forma de pagamento;
- características relacionadas ao relacionamento e perfil do cliente.

A variável `customerID` não é utilizada pelo modelo por representar apenas um identificador.

## 7. Decisão apoiada pelo modelo

Para cada cliente, o modelo estima uma probabilidade de churn.

Clientes cuja probabilidade seja igual ou superior a 0,40 são classificados como churn e podem ser priorizados para análise ou ações de retenção.

O modelo funciona como instrumento de apoio à decisão. A classificação não representa uma decisão automática sobre o cliente e deve ser combinada com critérios e estratégias definidos pela área de negócio.

## 8. Riscos e limitações

Os principais riscos considerados são:

- falsos positivos, levando à abordagem de clientes que não cancelariam;
- falsos negativos, deixando de identificar clientes que efetivamente apresentarão churn;
- alteração do comportamento dos clientes ao longo do tempo;
- diferença entre os dados utilizados no desenvolvimento e dados encontrados em um ambiente real;
- utilização das previsões sem considerar o custo e o benefício das ações de retenção.

O desempenho do modelo deve ser monitorado caso a solução seja utilizada com novos dados.

## 9. Critério de sucesso

O sucesso técnico da solução é avaliado principalmente pelo F1-score, complementado por ROC-AUC, precision e recall.

Do ponto de vista de negócio, uma implementação real deverá avaliar se a priorização produz redução da taxa de churn e aumento da retenção em relação a uma estratégia sem utilização do modelo.

A efetividade de negócio somente poderá ser confirmada após a utilização das previsões em ações reais de retenção e comparação dos resultados obtidos.