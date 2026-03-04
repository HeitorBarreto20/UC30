animal = ["Cachorro", "Gato"]
print ("Lista inicial: ", animal)

animal.append ("Pato")
print ("Lista atualizada: ", animal) #adiciona o dado no final
animal.insert(1, "Coelho")
print ("Lista atualizada: ", animal) #adiciona o dado em qualquer posição

animal.extend (["Macaco", "Leão"]) #adiciona mais de um dado no final
print ("Lista atualizada: ", animal)

animal.remove ("Leão")
print (animal)

removido = animal.pop()
print (f"Removido: {revomido}")
print ("Após pop()", animal)

removido2 = animal.pop(1)
print (f"Removido do índice 1 {removido2}")
print ("Ápos pop(1): ", animal)

del animal[0]
print ("Após o del ", animal)

animal.clear()
print (animal)