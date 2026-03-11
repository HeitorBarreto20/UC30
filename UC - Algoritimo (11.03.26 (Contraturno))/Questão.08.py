preço = int (input("Digite o preço do produto: "))

if preço < 100: 
    desconto = 0
elif preço  >= 100 and preço < 500:
    desconto = preço * 0.05
elif preço >= 500 and preço < 1000:
    desconto = preço * 0.10
elif preço >= 1000: 
    desconto = preço * 0.15
else:
    desconto = preço * 0.20

valorfinal = preço - desconto

print (f"O preço foi total da compra foi: {valorfinal}!")