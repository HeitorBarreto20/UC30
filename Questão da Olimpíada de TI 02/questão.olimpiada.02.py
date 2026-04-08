infectados_no_inicio = int(input("Qual o número inicial de infectados?"))
fator_de_reprodução = int(input("Quantas pessoas uma pessoa infectada consegue infectar?"))
meta_de_infectados = int(input("Qual é a meta de infectados?"))

total_de_infectados = infectados_no_inicio
infectados_do_dia = infectados_no_inicio
dias_que_passaram = 0

while total_de_infectados < meta_de_infectados:
    infectados_do_dia = infectados_do_dia * fator_de_reprodução
    total_de_infectados += infectados_do_dia
    dias_que_passaram += 1

print (f"Precisa de {dias_que_passaram} para transformar todo mundo em zumbi!")