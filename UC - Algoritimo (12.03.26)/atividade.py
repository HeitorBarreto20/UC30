def numero(numero01, numero02):
    soma = numero01 + numero02
    produto = numero01 * numero02

    return soma, produto

soma, produto = numero(10, 20)

print (f"O resultado da soma é: {soma}!")
print (f"O resultado da multiplicação é: {produto}!")