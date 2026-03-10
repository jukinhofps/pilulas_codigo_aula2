import random

cotacao = float(input("Digite a cotação do dolar: ")) # Cotação do dolar
taxa = (random.uniform(-1.5, 1.5)/100) # Taxa de variação
novaCotacao = cotacao * (1 + taxa) # Nova cotação

print(f"A taxa de variacao foi: {taxa:.3f}%")
print(f"A nova cotação é: R$ {novaCotacao:.2f}")