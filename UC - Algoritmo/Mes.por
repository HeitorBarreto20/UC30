programa {
    funcao inicio () {
        inteiro mes

        escreva ("Digite um número de 1 a 12:")
        leia (mes)

        escolha (mes){
            caso 1: caso 3: caso 5: caso 7: caso 8: caso 10: caso 12:
            escreva ("Esse mês tem 31 dias!")
            pare

            caso 2:
            escreva ("Esse mês tem 28 ou 29 dias!")
            pare

            caso 4: caso 6: caso 9: caso 11:
            escreva ("Esse mês tem 30 dias!")

            caso contrario:
            escreva ("Está mês tem 0 dias, pois não existe!")
        }
    }
}