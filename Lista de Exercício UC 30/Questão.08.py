preço = float(input("Qual o valor do negócio que tu comprou? "))

if preço > 500:
    preço_final = preço * 0.8
elif preço <= 500 and preço >= 200:
    preço_final = preço * 0.9
else:
    preço_final = preço

print (f"O preço final foi: {preço_final}!")