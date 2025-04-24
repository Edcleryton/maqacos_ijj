#Mini Case: Idade do Pet e Lucro do PETSHOP
print("Ola, seja bem vindo!")
print("Para melhor te ajudar, preciso de algumas informações.")
nome_do_tutor = input("Digite o nome do tutor: ").lower()
nome_do_pet = input("Digite o nome do pet: ").lower()
idade = int(input("Agora digite a idade do cachorro: "))
idade_pet = idade * 7

porte_pet = input("Qual o porte do pet? (pequeno, médio ou grande): ")
if porte_pet == "pequeno":
    valor_banho = 50.00 
    custo_banho = 5.00
elif porte_pet == "medio":   
    valor_banho = 60.00
    custo_banho = 15.00
elif porte_pet == "grande":
    valor_banho = 75.00
    custo_banho = 20.00 
else:
    print("Porte inválido. Por favor, digite pequeno, médio ou grande.")
  
   
quantidade_banhos = int(input("Digite a quantidade de banhos que o pet tomou nos ultimos 12 meses: "))
lucro = valor_banho * quantidade_banhos - custo_banho * quantidade_banhos
print(f"Olá, {nome_do_pet .capitalize()}, pertence a(ao) {nome_do_tutor .capitalize()} , e tem {idade_pet} anos, e nos últimos 12 meses o lucro com este animal foi de R${lucro:.2f}.")
print("Obrigado por utilizar nosso sistema!")
print("Até logo!")