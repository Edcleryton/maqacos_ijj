# Solicitando o valor ao usuário
print("Olá, vamos calcular suas notas?")
nome = input("Digite seu nome: ")

def validar_nota(numero):
    while True:
        nota = input(f"Digite a {numero}ª nota (0-10): ").replace(',', '.')  # Aceita vírgula ou ponto
        try:
            nota = float(nota)
            if 0 <= nota <= 10:
                return nota
            print("⚠️ Nota fora do intervalo! Deve ser entre 0 e 10.")
        except ValueError:
            print("⚠️ Digite um número válido (ex: 7.5 ou 9.0).")

nota1 = validar_nota(1)
nota2 = validar_nota(2)
nota3 = validar_nota(3)
nota4 = validar_nota(4)

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"Olá, {nome}! Sua média é: {media:.1f} pontos")