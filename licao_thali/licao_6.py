valor = float(input("Digite um número: ").replace(",", "."))

dobro = (valor * 2)
triplo = (valor * 3)
quadrado = (valor * valor)
raiz_quadrada = (valor ** 0.5)
raiz_cubica = (valor ** (1/3))

print("_______________________________________")
print(f"Dobro: {dobro: .2f}")
print("_______________________________________")
print(f"Triplo: {triplo: .2f}")
print("_______________________________________")
print(f"Quadrado: {quadrado: .2F}")
print("_______________________________________")
print(f"Raiz quadrada: {raiz_quadrada: .2f}")
print("_______________________________________")
print(f"Raiz cúbica: {raiz_cubica: .2f}")