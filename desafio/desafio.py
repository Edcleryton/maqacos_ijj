# 1 - Filtragem e Transformação de Listas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def eh_par(x):
    return x % 2 == 0

def multiplicar_por_dois(x):
    return x * 2

pares = filter(eh_par, numeros)
dobrados = map(multiplicar_por_dois, pares)
resultado1 = sorted(dobrados, reverse=True)

print("Solução 1:", list(resultado1))

# 2 - Filtragem e Transformação de Tuplas (Strings e Inteiros)
dados = ("maçã", 10, "banana", 5, "laranja", "uva", 20)

def eh_string(x):
    return isinstance(x, str)

def para_maiuscula(x):
    return x.upper()

strings = filter(eh_string, dados)
maiusculas = map(para_maiuscula, strings)
resultado2 = tuple(sorted(maiusculas))

print("Solução 2:", resultado2)

# 3 - Filtragem e Transformação de Sets
palavras = {"banana", "Abacate", "pera", "Amora", "uva", "aveia"}

def comeca_com_a(x):
    return x.lower().startswith("a")

def para_maiuscula_str(x):
    return x.upper()

com_a = filter(comeca_com_a, palavras)
maiusculas = map(para_maiuscula_str, com_a)
resultado3 = set(sorted(maiusculas))

print("Solução 3:", resultado3)

# 4 - Filtragem e Transformação de Valores de Dicionário
dicionario = {"a": 10, "b": "banana", "c": "abacaxi", "d": 5, "e": "uva", "f": "melancia"}

valores = dicionario.values()

def string_maior_que_tres(x):
    return isinstance(x, str) and len(x) > 3

def para_minuscula(x):
    return x.lower()

filtrados = filter(string_maior_que_tres, valores)
minusculas = map(para_minuscula, filtrados)
resultado4 = sorted(minusculas)

print("Solução 4:", resultado4)
