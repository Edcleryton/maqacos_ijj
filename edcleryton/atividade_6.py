#Operações de teste
print("Olá vamos realizar alguns cálculos")
numero = float(input("Insira um número qualquer aqui: ").replace(',', '.'))

dobro = numero * 2
triplo = numero * 3
quadrado = numero ** 2
raiz_quadrada = numero ** (1/2)
raiz_cubica = numero ** (1/3)

print(f"Dobro do valor inserido: {dobro}.")
print(f"Triplo do valor inserido: {triplo}.")
print(f"Valor inserido ao quadrado: {quadrado}.")
print(f"Raiz quadrada do valor inserido: {raiz_quadrada:.2f}.")
print(f"Raiz cúbica do valor inserido: {raiz_cubica:.2f}.")