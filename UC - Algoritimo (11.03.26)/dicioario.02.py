contato = {
    "@camila": "Camila",
    "@paola": "Paola",
    "@sheron": "Sheron",
    "@bruna": "Bruna",
    "@joao": "João"
}

#Obter chaves
print ("Chaves: ")
for insta in contato.keys():
    print (insta)

#obter valores
print ("\n Valores: ")
for nome in contato.values():
    print (nome)

#obter pares
print ("\n Pares: ")
for insta, nome in contato.items():
    print (f"{insta} --> {nome}")

contato = {
    "@camila": 1.80,
    "@paola": 1.30,
    "@sheron": 1.40,
    "@bruna": 1.60,
    "@joao": 1.70
}

#ordenar por chave 
print ("Ordenar por chave: ")
for insta in sorted (contato.keys()):
    print (f"{insta} --> {contato[insta]:.2f}m")

#ordenar por valor
from operator import itemgetter
print ("\n Ordenada por valor (altura): ")
for insta, estatura in sorted (contato.items(), key=itemgetter(1)):
    print(f"{insta} --> {estatura:.2f}m")