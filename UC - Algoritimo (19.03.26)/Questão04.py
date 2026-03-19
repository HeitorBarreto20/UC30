def pontuacao_total(pontos, tempo):

    if tempo < 30:
        pontos += 50

    elif tempo > 100:
        pontos -= 20

    elif pontos > 200:
        return "Recorde"
    
    else:
        return pontos
