temperaturas = [20, 21, 22, 23, 24, 25, 26]

soma = 0

for temp in temperaturas:
    soma += temp

media = soma / len(temperaturas)

print(f"A média das temperaturas é: {media}°C")