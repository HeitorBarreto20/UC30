def compras ():
    try:
        preço01 = float(input("Qual o preço do primeiro produto?"))
        preço02 = float(input("Qual o preço do segundo produto?"))

        total = preço01 + preço02
        print (f"O preço da sua compra foi {total}!")

    except ValueError:
        print ("Erro: Coloque números PELO AMOR DE DEUS!")

compras()