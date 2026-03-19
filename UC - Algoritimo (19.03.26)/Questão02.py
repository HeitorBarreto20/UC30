def saldo_final(saldo, saque):

    if saque > saldo:
        return "Você é pobre!"
    
    elif saque > 1000:
        taxa = saque * 0.02
        saque_total = saque + taxa
    else:
        saque_total = saque
    
    saldo_restante = saldo - saque_total
    
    return saldo_restante