print("olá, vamos calcular suas notas?")
nomealuno=str(input("Digite aqui seu nome completo: "))
nota1 = int(input("Digite aqui a sua primeira nota: "))
nota2 = int(input("Digite aqui a sua segunda nota: "))
nota3 = int(input("Digite aqui a sua terceira nota: "))
nota4 = int(input("Digite aqui a sua quarta nota: "))

soma = nota1 + nota2 + nota3 + nota4 # Somando as notas
media = soma / 4 # Calculando a média

print(f"Olá, {nomealuno}! Sua média é: {media} pontos")

