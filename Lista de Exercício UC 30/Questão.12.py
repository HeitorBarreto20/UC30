def calculadora():
    try:

        print ("\n--- Calculadora ---")
        print ("1: Soma")
        print ("2: Subtração")
        print ("3: Multiplicação")
        print ("4: Divisão")
        print ("0: Sair")

        escolha = int(input("Qual calculo você quer realizar? "))

        if escolha == 0:
            print ("Saindo do site!")

        if escolha [1, 2, 3, 4]:
            n1 = float (input("Digite o primeiro número: "))
            n2 = float (input("Digite o segundo número: "))

        soma = n1 + n2
        subtração = n1 - n2
        multiplicação = n1 * n2
        divisão = n1 / n2

        if escolha == 1:
            print (f"{n1} mais {n2} é igual a {soma}!")
        elif escolha == 2:
            print (f"{n1} menos {n2} é igual a {subtração}!")
        elif escolha == 3:
            print (f"{n1} vezes {n2} é igual a {multiplicação}!")
        else:
            print (f"{n1} dividido por {n2} é igual a {divisão}!")

    except ValueError:
        print ("Erro!")