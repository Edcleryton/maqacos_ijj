import pandas as pd

# Certifique-se de que o arquivo 'dados.csv' exista no diretório correto
df = pd.read_csv('dados.csv')

# Exiba as primeiras linhas do DataFrame para confirmar que funcionou
print('dados iniciais')
print(df.head())
