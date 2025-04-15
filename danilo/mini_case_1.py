# Mini Case 1: Idade do Pet e Lucro do PETSHOP
print("Calculadora de Idade de Pet e Lucro do Petshop")
nome_pet = input("Digite o nome do pet: ").capitalize()
idade_humana = int(input("Digite a idade humana do pet (em anos): "))
porte = input("Digite o porte do cachorro (grande, médio ou pequeno): ") 
numero_banhos = int(input("Digite o número de banhos nos últimos 12 meses: "))

# Calcula a idade do pet em "anos de cachorro"
idade_pet = idade_humana * 7

# Define os valores de banho e custo conforme o porte (agora com maiúscula na primeira letra)
if porte == 'Grande':  # Alterado para 'Grande'
    valor_banho = 75
    custo_banho = 20
elif porte == 'Médio':  # Alterado para 'Médio'
    valor_banho = 60
    custo_banho = 15
else:  # Assume 'Pequeno' como padrão
    valor_banho = 50
    custo_banho = 5

# Calcula o lucro
lucro = (valor_banho - custo_banho) * numero_banhos

# Exibe o resultado formatado
print(f"Olá, {nome_pet} tem {idade_pet} anos e nos últimos 12 meses o lucro com este animal foi de R${lucro:.2f}")
