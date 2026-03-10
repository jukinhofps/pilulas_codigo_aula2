import datetime

dataCompra = input("Digite a data da compra (DD/MM/AAAA): ") # Data da compra
garantia = int(input("Digite o prazo da garantia em meses: ")) # Prazo da garantia
dataInicio = datetime.datetime.strptime(dataCompra, "%d/%m/%Y") # Data de inicio
dataFinal = dataInicio + datetime.timedelta(days = garantia * 30) # Data final

print(f"A data final da garantia: {dataFinal.strftime('%d/%m/%Y')}")
print(f"Dia da semana: {dataFinal.strftime('%A')}")