# Solicitando o valor ao usuário
valor = int(input("Digite um número inteiro qualquer: "))

# Calculando os resultados
dobro = valor * 2
triplo = valor * 3
quadrado = valor ** 2
raiz_quadrada = valor ** 0.5
raiz_cubica = valor ** (1/3)

# Exibindo os resultados
print(f"1. Dobro do valor: {dobro}")
print(f"2. Triplo do valor: {triplo}")
print(f"3. Valor ao quadrado: {quadrado}")
print(f"4. Raiz quadrada: {raiz_quadrada:.2f}")  # Arredondando para 2 casas decimais
print(f"5. Raiz cúbica: {raiz_cubica:.2f}")   