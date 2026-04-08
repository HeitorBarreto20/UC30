pão = int(input(f"Quantos pães você vendeu?"))
doce = int(input(f"Quantos doces você vendeu?"))
bolo = int(input(f"Quantos bolos você vendeu?"))

pontos = (pão * 1) + (doce * 2) + (bolo * 3)

if pontos >= 150:
    print (f"Sua pontuação foi {pontos} e vocês vão ganhar um bolo!")
elif pontos >= 120:
    print (f"Sua pontuação foi {pontos} e vocês vão ganhar um doce!")
elif pontos >= 100:
     print (f"Sua pontuação foi {pontos} e vocês vão ganhar um mísero pão!")
else:
    print (f"Sua pontuação foi {pontos} e vocês não vão ganhar bosta nenhuma")