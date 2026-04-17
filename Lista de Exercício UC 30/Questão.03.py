total = 0.0

print("Lista de compras, digite o valor dos seus produtos: ")

while True:
    valor = float(input("Valor do item: "))

    if valor == 0:
        break
    
    total += valor

print(f"O valor total da compra é: {total}!")