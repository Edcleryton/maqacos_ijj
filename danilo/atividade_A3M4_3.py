# Faça um programa que capture o nome do usuário, altura em metros, idade e imprima esses dados na tela.
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros (ex: 1.76): "))
idade = int(input("Digite sua idade: "))

print(f"Nome do usuário: {nome}, sua altura é {altura}, sua idade é: {idade}")

# Agora, implemente uma nova Feature: a funcionalidade de notas.
nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))

media_notas = (nota1 + nota2) / 2

print(f"Sua media final foi de {media_notas}")

print(f"Tipo de variável media_notas recebe: {type(media_notas)}")
print(f"Tipo de váriável nome recebe: {type(nome)}")
print(f"Tipo de váriável idade recebe: {type(idade)}")