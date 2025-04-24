# 1 - Filtragem e Transformação de Listas
# Função para filtrar pares e multiplicar por 2
def filtrar_e_transformar(numeros):
    numeros_pares = []
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)

    numeros_multiplicados = []
    for numero in numeros_pares:
        numeros_multiplicados.append(numero * 2)

    return numeros_multiplicados

# Função para ordenar e exibir o resultado
def ordenar_e_exibir(lista):
    resultado = []
    for numero in sorted(lista, reverse=True):
        resultado.append(numero)
    print("Solução 1:", resultado)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

transformados = filtrar_e_transformar(numeros)
ordenar_e_exibir(transformados)


# 2 - Filtragem e Transformação de Tuplas (Strings e Inteiros)
dados = ("maçã", 10, "banana", 5, "laranja", "uva", 20)

# Filtragem: Remover números inteiros
apenas_strings = []
for elemento in dados:
    if isinstance(elemento, str):
        apenas_strings.append(elemento)

# Transformação: Converter strings para maiúsculas
strings_maiusculas = []
for string in apenas_strings:
    strings_maiusculas.append(string.upper())

# Ordenação: Ordenar alfabeticamente
resultado = []
for string in sorted(strings_maiusculas):
    resultado.append(string)

resultado = tuple(resultado)
print("Solução 2:", resultado)  # Saída: ('BANANA', 'LARANJA', 'MAÇÃ', 'UVA')

# Filtragem e Transformação de Sets
palavras = {"banana", "Abacate", "pera", "Amora", "uva", "aveia"}

# Filtragem: Selecionar palavras que começam com "a" ou "A"
palavras_filtradas = []
for palavra in palavras:
    if palavra.lower().startswith('a'):
        palavras_filtradas.append(palavra)

# Transformação: Converter para maiúsculas
palavras_maiusculas = []
for palavra in palavras_filtradas:
    palavras_maiusculas.append(palavra.upper())

# Ordenação: Ordenar alfabeticamente
resultado = []
for palavra in sorted(palavras_maiusculas):
    resultado.append(palavra)

resultado = set(resultado)
print("Solução 3:", resultado)  # Saída: {'ABACATE', 'AMORA', 'AVEIA'}

#Filtragem e Transformação de Valores de Dicionário
dicionario = {"a": 10, "b": "banana", "c": "abacaxi", "d": 5, "e": "uva", "f": "melancia"}

# Filtragem: Selecionar valores que são strings com comprimento > 3
valores_filtrados = []
for valor in dicionario.values():
    if isinstance(valor, str) and len(valor) > 3:
        valores_filtrados.append(valor)

# Transformação: Converter para minúsculas
valores_minusculos = []
for valor in valores_filtrados:
    valores_minusculos.append(valor.lower())

# Ordenação: Ordenar alfabeticamente
resultado = []
for valor in sorted(valores_minusculos):
    resultado.append(valor)

print("Solução 4:", resultado)  # Saída: ['abacaxi', 'banana', 'melancia']


















































