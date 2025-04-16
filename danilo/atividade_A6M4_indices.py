#Em lista, imprimimos os indices assim:
idades = [10, 15, 21, 18, 20]

#Desafio: Imprima em For os indices
for index, idade in enumerate(idades):
    if idade >= 18:
        print (f"Indivíduo possui idade mínima para dirigir, {idade} anos, índice {index}")