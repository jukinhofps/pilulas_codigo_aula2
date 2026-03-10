import statistics

lote1 = float(input("Digite o valor do lote 1: ")) # Ler os valores do lote 1
lote2 = float(input("Digite o valor do lote 2: ")) # Ler os valores do lote 2
lote3 = float(input("Digite o valor do lote 3: ")) # Ler os valores do lote 3

media = statistics.mean( (lote1, lote2, lote3) ) # Calcular a media
desvio = statistics.stdev( (lote1, lote2, lote3) ) # Calcular o desvio

print(f"A media é: {media:.2f}")
print(f"O desvio padrao é: {desvio:.2f}")