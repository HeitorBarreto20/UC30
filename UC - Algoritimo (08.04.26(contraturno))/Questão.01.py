mesada = int(input(f"Qual sua mesada?"))
alimentação = int(input(f"Quanto você gastou em alimentação?"))
transporte = int(input(f"Quanto você gastou em transporte?"))
lazer = int(input(f"Quanto você gastou em lazer?"))

valor_total = alimentação + transporte + lazer

if valor_total < mesada:
    print (f"Você está individado, vai passar fome e morrer!")
elif valor_total > mesada:
    print (f"Você conseguiu pagar as contas, não fez mais que o necessário!")
else:
    print (f"Você consegiu pagar as contas, mas quase passou fome!")