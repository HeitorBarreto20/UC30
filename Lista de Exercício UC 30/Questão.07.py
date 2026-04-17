vendas = [143, 29, 52, 1036, 283, 1, 566]

soma = 0

for valores in vendas:
    if valores % 2 == 0:
        soma += valores

print (f"A soma dos valores pares é {soma}!")