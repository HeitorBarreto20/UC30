aluno = {}

aluno ["nome"] = input ("Digite seu nome: ")
aluno ["nota01"] = float (input("Digite a primera nota: "))
aluno ["nota02"] = float (input("Digite a segunda nota: "))

media = (aluno["nota01"] + aluno["nota02"]) / 2

aluno["media"] = media

if aluno["media"] >= 7:
    resultado = "Aprovado"
elif aluno["media"] >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print ("\n Coisas do aluno:")
print ("Nome: ", aluno["nome"])
print ("Nota01: ", aluno["nota01"])
print ("Nota02: ", aluno["nota02"])
print ("Média: ", aluno["media"])
print ("Está: ", resultado)