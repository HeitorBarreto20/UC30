programa {
    funcao inicio () {

        inteiro valorcasa, salario, prestacao
        real anos, meses

        escreva ("Qual o valor da casa que você vai comprar? ")
        leia (valorcasa)
        escreva ("Quanto você ganha? ")
        leia (salario)
        escreva ("Em quantos anos você vai pagar a casa? ")
        leia (anos)

        meses = anos * 12
        prestacao = valorcasa / meses

        escreva ("O valor da prestação é ", prestacao, "!")

        se (prestacao <= salario * 0.30) {
        escreva ("Emprestimo aprovado!")
        }

        senao {
            escreva ("Emprestimo não aprovado!")
        }
    }
}