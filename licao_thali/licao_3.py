primeiro_nome = input("Insira o primeiro nome do cliente: ")
sobrenome = input("Insira o sobrenome do cliente: ")
nome_cliente = primeiro_nome + " " + sobrenome


valor_compra = input("Insira o valor da compra: ").replace(",", ".")
valor_compra = float(valor_compra)

cupom = primeiro_nome.upper()

mensagem = f"Olá, {nome_cliente}. Em JANEIRO você realizou uma compra no valor de R${valor_compra:.2f} e ganhou um desconto de 10% em sua próxima compra. Use o cupom {cupom}É10."

print(mensagem)