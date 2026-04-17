try:
    peso = float(input("Qual seu peso? "))
    
    if peso <= 24.9:
        print ("Você é magro!")
    else:
        print ("Você está bem!")

except ValueError:
    print("Erro: Você digitou algo que não pode!")