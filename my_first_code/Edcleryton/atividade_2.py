# Definindo as variáveis
nome_cliente = "Maria"
valor_compra = 500.00
desconto = 10  # 10%

# Criando o cupom (ex: MAR10)
cupom = nome_cliente[:3].upper() + str(desconto)

# Mensagem personalizada
print("Olá,", nome_cliente + "!")
print("Em JANEIRO você realizou uma compra no valor de R$", valor_compra)
print("e ganhou um desconto de", desconto, "'%'  em sua próxima compra.")
print("Use o cupom", cupom)