nome = input("Digite seu nome: ")
altura = input("Digite sua altura em metros: ").replace(",", ".")
altura = float(altura)
idade = int(input("Digite sua idade: "))

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
soma = nota1 + nota2  
media = (nota1 + nota2) / 2

print("\n--- Dados do Usuário ---")
print(f"Nome: {nome}")
print(f"Altura: {altura:.2f} metros")
print(f"Idade: {idade} anos")
print(f"Soma das notas: {soma:.2f}")
print(f"Média das notas: {media:.2f}")

tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)

print("Tipo de dado de 'nome':", tipo_nome)
print("Tipo de dado de 'idade':", tipo_idade)
print("Tipo de dado de 'altura':", tipo_altura)

