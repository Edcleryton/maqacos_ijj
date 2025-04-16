nota = int(input("Insira um número inteiro aleatório: ")) 

conta1 = nota * 2
conta2 = nota * 3
conta3 = nota ** 2
conta4 = nota ** (1/2)
conta5 = nota ** (1/3)

print (f"Dobro do valor: {conta1}")
print (f"Triplo do valor: {conta2}")
print (f"Valor ao quadrado: {conta3}")
print (f"Raiz quadrada do valor: {conta4:.2f}")
print (f"Raiz cúbica do valor: {conta5:.2f}")