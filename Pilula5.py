import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

receita1 = float(input("Digite a receita do primeiro trimestre: ")) # Receita do primeiro trimestre
receita2 = float(input("Digite a receita do segundo trimestre: ")) # Receita do segundo trimestre
receita3 = float(input("Digite a receita do terceiro trimestre: ")) # Receita do terceiro trimestre

total = (receita1 + receita2 + receita3) # Total das receitas

print(f"Mês 1 {locale.currency(receita1,grouping=True)}")
print(f"Mês 2 {locale.currency(receita2,grouping=True)}")
print(f"Mês 3 {locale.currency(receita3,grouping=True)}")
print(f"Total {locale.currency(total,grouping=True)}")
