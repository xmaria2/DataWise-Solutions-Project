import pandas as pd

def analyze_data(df):
    summary = df.describe()
    return summary

# Exemplo de uso
df = pd.read_csv('data_cleaned.csv')
summary = analyze_data(df)
print(summary)
