frase = input("Digite qualquer frase: ")

vogais = "aeiou"

total_vogais = 0

for letras in frase:
    if letras.lower() in vogais:
        total_vogais += 1

print(f"A frase que tu digitou tem {total_vogais} vogais!")