aluno = input("Entre com seu nome: ")
print("_________________________________________________")
print(f"Seja bem vindo(a) {aluno}!")
print("_________________________________________________")
nota_1 = float (input("Por favor digite a sua primeira nota: ").replace(",", "."))
nota_2 = float (input("Digite a segunda nota: ").replace(",", "."))
nota_3 = float (input("Digite a terceira nota: ").replace(",", "."))
nota_4 = float (input("Digite a quarta nota: ").replace(",", "."))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f"Olá {aluno}! Sua média é: {media: .2f} pontos.")