# Criado uma lista para armazenar as informações dos clientes 
clientes = [
    {"nome": "PAULA MARTINS", "mes": "JANEIRO", "valor": 500.00},
    {"nome": "CARLOS SILVA", "mes": "FEVEREIRO", "valor": 320.00},
    {"nome": "ANA SOUZA", "mes": "MARÇO", "valor": 750.00}
]

# Criado um for para percorre a lista e gerar as mensagens
for cliente in clientes:
    nome = cliente["nome"]
    mes = cliente["mes"]
    valor = cliente["valor"]
    
    cupom = nome.split()[0].upper() + "É10"

    mensagem = f"Olá, {nome}. Em {mes} você realizou uma compra no valor de R${valor:.2f} e ganhou um desconto de 10% em sua próxima compra. Use o cupom {cupom}."
    
    print(mensagem, "\n")
