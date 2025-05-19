import pandas as pd

#df = pd.read_csv('edcleryton/dados.csv')


#print("Dados iniciais:")
#print(df.head())

#filtro_idade = df[df['idade'] > 25]
#print("\nPessoas com mais de 25 anos:")
#print(filtro_idade)

#df_ordenado = df.sort_values(by='idade', ascending=False)

#df_ordenado.to_csv('dados_processados.csv', index=False)

#print("\nArquivo 'dados_processados.csv' gerado com sucesso!")



df = pd.read_csv('edcleryton/dados_ficticios.csv')

print("Tipos de dados originais:")
print(df.dtypes)

df['idade'] = df['idade'].str.strip()  
df['idade'] = pd.to_numeric(df['idade'], errors='coerce')  
df = df.dropna(subset=['idade'])  

print("\nTipos de dados após limpeza:")
print(df.dtypes)

# Aplicar filtros
filtro_idade = df[df['idade'] > 40]
print("\nPessoas com mais de 40 anos:")
print(filtro_idade)

filtro_renda_5k = df[df['renda'] > 5000]
print("\nPessoas com renda maior que 5 mil:")
print(filtro_renda_5k)

filtro_renda_15k = df[df['renda'] > 15000]
print("\nPessoas com renda maior que 15 mil:")
print(filtro_renda_15k)


df_ordenado = df.sort_values(by='idade', ascending=False)

df_ordenado.to_csv('edcleryton/dados_processados.csv', index=False)

print("\nArquivo 'dados_processados.csv' gerado com sucesso!")