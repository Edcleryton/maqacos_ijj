# Capturando os dados do usuário
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite sua idade: "))

# Nova feature: Capturando notas
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
soma = nota1 + nota2  # Somando as notas
media = (nota1 + nota2) / 2 # Calculando a média

#  identificando o tipo de dado das variavéis

tipo_nome = type(nome)
tipo_idade = type(idade) 
tipo_altura = type(altura) 
tipo_nota1 = type(nota1)
tipo_nota2 = type(nota2)
tipo_soma = type(soma)
tipo_media = type(media)

# Exibindo todos os dados
print("\n--- Dados do Usuário ---")
print("Nome:", nome)
print("Altura:", altura, "metros")
print("Idade:", idade, "anos")
print("Soma das notas:", soma)
print("Média das notas:", media)

# Tipo dos dados
print("Tipo de dado do 'nome':", tipo_nome) 
print("Tipo de dado da 'idade':", tipo_idade) 
print("Tipo de dado da 'altura':", tipo_altura)
print("Tipo de dado da 'nota1':", tipo_nota1)
print("Tipo de dado da 'nota2':", tipo_nota2)
print("Tipo de dado da 'soma':", tipo_soma)
print("Tipo de dado da 'media':", tipo_media)