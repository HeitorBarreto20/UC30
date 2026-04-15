def media():
    notas = []
    try:
        nota01 = float(input("Digite sua primeira nota: "))
        nota02 = float(input("Digite sua segunda nota: "))
        nota03 = float(input("Digite sua terceira nota: "))
        
        notas.append(nota01)
        notas.append(nota02)
        notas.append(nota03)
    
        media = (nota01 + nota02 + nota03) / 3
        print(f"Sua média foi {media}!")

    except ValueError:
        print("Erro: Você digitou algo que não pode!")

media()