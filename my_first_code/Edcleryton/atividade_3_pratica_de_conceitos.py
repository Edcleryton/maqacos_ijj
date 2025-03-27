# Capturando os dados do usuário
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite sua idade: "))

# Nova feature: Capturando notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
soma = nota1 + nota2  # Somando as notas

# Exibindo todos os dados
print("\n--- Dados do Usuário ---")
print("Nome:", nome)
print("Altura:", altura, "metros")
print("Idade:", idade, "anos")
print("Soma das notas:", soma)