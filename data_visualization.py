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
