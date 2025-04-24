#RESPOSTA SIMPLES
nome = "Paula Martins"
mes = "Janeiro"
valor_compra = 500
desconto = 10
cupom = "PAULAÉ10"

mensagem = f"Olá, {nome}. Em {mes} você realizou uma compra no valor de R${valor_compra:.2f} e ganhou um desconto de {desconto}% em sua próxima compra. Use o cupom {cupom}."
print(mensagem)

#RESPOSTA COMPLETA
# Entrada de dados corrigida
customer_name = input("Digite o nome do cliente: ")
month = input("Digite o mês da compra: ")
purchase_value = float(input("Digite o valor da compra: "))
discount = int(input("Digite o percentual de desconto (máximo 40%): "))

# Validar o desconto (limite de 40%)
if discount > 40:
    discount = 40  # Define 40% se o valor for maior
elif discount < 0:
    discount = 0   # Evita valores negativos

# Gerar o cupom com o desconto validado
primeiro_nome = customer_name.split()[0]
coupon = primeiro_nome.upper() + "É" + str(discount)  # Usa o desconto validado

# Mensagem personalizada com o desconto validado
message = f"""
Olá, {customer_name}!
Em {month} você realizou uma compra no valor de R${purchase_value:.2f}
e ganhou um desconto de {discount}% em sua próxima compra.
Use o cupom {coupon}."""

print(message)