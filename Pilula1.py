import math

assinantes = int(input("Digite o numero de assinantes: ")) # Numero atul de assinantes 
valor = float(input("Digite o valor da mensalidade: ")) # Valor da mensalidade
taxa = (float(input("Digite a taxa média de crescimento mensal de assinantes: "))/100) # taxa média de crescimento mensal de assinantes (em %) 
meses = int(input("Digite o numero de meses para projeção: ")) # Numero de meses para projeção

assinantesFinais = assinantes * math.pow((1 + taxa), meses) # Calculo dos assinantes finais
receitaFinal = assinantesFinais * valor # Calculo da receita final

print(f"Assinantes estimados: {assinantesFinais:.0f}")
print(f"Valor da receita final: R$ {receitaFinal:.2f}")