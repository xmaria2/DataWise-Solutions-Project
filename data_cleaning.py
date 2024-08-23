
### 1. Limpeza de Dados (`data_cleaning.py`)

import pandas as pd

def clean_data(df):
    # Remove duplicatas
    df = df.drop_duplicates()
    # Preenche valores ausentes
    df = df.fillna(method='ffill')
    return df

# Exemplo de uso
df = pd.read_csv('data.csv')
df_cleaned = clean_data(df)
df_cleaned.to_csv('data_cleaned.csv', index=False)

### Script: `data_cleaning.py`
Este script foi desenvolvido para realizar a limpeza dos dados brutos, removendo duplicatas e preenchendo valores ausentes.

#### Objetivo
O objetivo deste script é garantir que os dados utilizados nas análises subsequentes estejam limpos e preparados, evitando problemas como duplicidade de informações e valores ausentes que poderiam distorcer os resultados da análise.

#### Uso no Projeto
O script `data_cleaning.py` foi utilizado logo após a obtenção dos dados brutos da base de dados da empresa. Após a leitura do arquivo `data.csv`, o script foi executado para limpar os dados antes de prosseguir com as etapas de análise e visualização.


#### Descrição do Código
- **Importação de Bibliotecas:** O script começa importando a biblioteca `pandas`, que é usada para manipulação de dados em DataFrames.
- **Função `clean_data`:** Esta função recebe um DataFrame como entrada, remove as duplicatas com `drop_duplicates()`, e preenche valores ausentes usando o método `ffill()`, que propaga o último valor válido.
- **Exemplo de Uso:** Um exemplo prático é dado, onde o script lê um arquivo CSV, executa a função de limpeza, e salva o DataFrame limpo em um novo arquivo.


    #### Resultados Obtidos
Após a execução do script, o arquivo `data_cleaned.csv` foi gerado, contendo um conjunto de dados livre de duplicatas e sem valores ausentes. Isso garantiu que as análises subsequentes fossem precisas e confiáveis, proporcionando uma base sólida para a visualização e a tomada de decisões.


#### Impacto no Projeto
A limpeza dos dados foi crucial para evitar inconsistências nos resultados da análise. Sem esta etapa, os dados poderiam conter erros que afetariam negativamente a precisão das previsões e insights obtidos na fase de análise de dados.

