### 1. Limpeza de Dados (`data_visualization.py`)

import matplotlib.pyplot as plt
import pandas as pd

def plot_data(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['value'])
    plt.title('Visualização de Dados')
    plt.xlabel('Data')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.savefig('plot.png')

# Exemplo de uso
df = pd.read_csv('data_cleaned.csv')
plot_data(df)

### Script: `data_visualization.py`
Este script foi desenvolvido para criar visualizações gráficas dos dados.

#### Objetivo
O objetivo deste script é transformar os dados analisados em gráficos que facilitam a compreensão visual das tendências e padrões identificados
durante a análise estatística.
    
#### Uso no Projeto
O script `data_visualization.py` Este script foi utilizado após a análise dos dados. Ele recebeu o DataFrame limpo e analisado como entrada e gerou gráficos,
como linhas de tempo, histogramas e gráficos de dispersão, que foram usados em relatórios e apresentações para ilustrar os principais achados do projeto.

#### Descrição do Código
Importação de Bibliotecas: O script faz uso das bibliotecas matplotlib e pandas. O matplotlib é utilizado para gerar os gráficos, enquanto o pandas é usado para manipular os dados.
Função plot_data: Esta função gera um gráfico de linha simples mostrando a variação de uma variável ao longo do tempo. 
A função personaliza o gráfico com títulos, rótulos e grades para melhorar a legibilidade.

    #### Resultados Obtidos
O script gerou gráficos que ilustraram claramente as tendências nos dados ao longo do tempo. Esses gráficos foram essenciais para comunicar os resultados
do projeto de maneira visualmente intuitiva, facilitando a compreensão dos padrões identificados.

#### Impacto no Projeto
As visualizações de dados criadas por este script ajudaram a transformar números abstratos em insights acionáveis. Isso não só tornou os dados mais acessíveis para os membros da equipe e partes interessadas, mas também melhorou a qualidade das decisões baseadas nos dados apresentados.
