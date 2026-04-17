notas = [5.5, 8.0, 7.0, 9.5, 6.2, 10.0, 7.1]

acima_de_sete = 0

for nota in notas:
    if nota > 7:
        acima_de_sete += 1

print(f"Quantidade de notas acima de 7: {acima_de_sete}")