import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Jogo de Adivinhação!")
print("Tente adivinhar um número de 1 a 100.")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("O número é MAIOR.")
    elif palpite > numero_secreto:
        print("O número é MENOR.")
    else:
        print(f" Parabéns! Você acertou em {tentativas} tentativas!")
        break

print("\n Agora digite 8 números:")

numeros = []

for i in range(8):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

contagem = {}

for n in numeros:
    if n in contagem:
        contagem[n] += 1
    else:
        contagem[n] = 1

repetidos = 0

print("\n Números repetidos:")
for num, qtd in contagem.items():
    if qtd > 1:
        print(f"O número {num} apareceu {qtd} vezes.")
        repetidos += 1

if repetidos == 0:
    print("Nenhum número foi repetido.")