import random

numeros = [1537, 3987, 4927, 2038, 5028, 6938]
print (numeros)

numeros.sort()
print ("Após sort(): ", numeros)

numeros.sort(reverse = True)
print ("Após sort(): ", numeros)

random.shuffle (numeros)
print ("Embaralhar: ", numeros)