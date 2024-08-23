## Scripts Desenvolvidos

### 1. Limpeza de Dados (`data_cleaning.py`)

```python
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
