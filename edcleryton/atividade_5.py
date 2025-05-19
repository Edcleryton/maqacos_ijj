# Solicitando o valor ao usuário
print("Olá, seja bem-vindo!")
print("Vamos verificar sua nota, para isso, preciso de algumas informações.")
print("Insira seu nome: ")
nome_aluno = str(input()).lower()
print("Insira a primeira nota: ")
nota1 = float(input())
print("Insira a segunda nota: ")
nota2 = float(input())
print("Insira a terceira nota: ")
nota3 = float(input())
print("Insira a quarta nota: ")
nota4 = float(input())
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"Olá, {nome_aluno.capitalize()}, sua média é: {media:.2f}!")

if media >= 7:
    print("Parabéns, você foi aprovado!")
elif media >= 5:
    print("Você está de recuperação.")
else:
    print("Infelizmente, você foi reprovado.")
exit()
