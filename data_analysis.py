### 1. Limpeza de Dados (`data_analysis.py`) 


import pandas as pd

def analyze_data(df):
    summary = df.describe()
    return summary

# Exemplo de uso
df = pd.read_csv('data_cleaned.csv')
summary = analyze_data(df)
print(summary)


### Script: `data_analysis.py`
Foi criado para realizar análises descritivas e estatísticas 
sobre os dados limpos.
    
#### Objetivo
O objetivo deste script é  identificar padrões, tendências, e 
fornecer um entendimento inicial sobre a distribuição
e características dos dados.
    
#### Uso no Projeto
Após a limpeza dos dados com o data_cleaning.py, este script 
foi utilizado para analisaro conjunto de dados.
Ele calculou estatísticas como média, mediana, desvio padrão, e 
identificou possíveis outliers. Isso foi essencial para orientar 
as próximas etapas de análise e visualização

#### Descrição do Código
Importação de Bibliotecas: O script utiliza a biblioteca pandas para manipulação de dados e análise estatística.
Função analyze_data: Esta função recebe um DataFrame e usa o método describe() do pandas para gerar um resumo estatístico, incluindo contagem, média, mínimo, 
máximo, e quartis para cada coluna numérica.

    #### Resultados Obtidos
O script gerou um resumo estatístico do conjunto de dados limpo. Esse resumo incluiu informações valiosas, como a média e o desvio padrão de cada variável, 
ajudando a identificar distribuições anômalas ou valores extremos que poderiam influenciar a análise.

#### Impacto no Projeto
A análise estatística fornecida por este script foi fundamental para entender a natureza dos dados, permitindo a identificação de tendências e padrões que guiaram as fases subsequentes do projeto. 



