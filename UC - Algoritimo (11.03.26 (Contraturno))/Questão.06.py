idade = int (input("Digite sua idade: "))

if idade < 12:
    print ("Você é da categoria infantil!")
elif idade >= 12 and idade < 18:
    print ("Você é da categoria juvenil!")
elif idade >= 18 and idade < 60:
    print ("Você é da categoria adulta!")
else:
    print ("Você é da categoria sênior!")