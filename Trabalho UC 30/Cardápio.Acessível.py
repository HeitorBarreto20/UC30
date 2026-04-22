cardapio = {
    1: ("Hambúrguer", 15),
    2: ("X-Burguer", 18),
    3: ("Batata Frita", 10),
    4: ("Hot Dog", 12),
    5: ("Pastel", 8),

    6: ("Água", 3),
    7: ("Refrigerante", 6),
    8: ("Suco", 7),
    9: ("Café", 4),
    10: ("Milkshake", 10),

    11: ("Sorvete", 8),
    12: ("Açaí", 12),
    13: ("Pudim", 7),
    14: ("Bolo", 6),
    15: ("Chocolate", 5)
}

pedido = []

def ler_numero(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print("Digite um número válido!")

def cadastro():
    print("\n--- CADASTRO ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    print("Cadastro realizado!\n")

def mostrar_cardapio():
    print("\n========== CARDÁPIO ==========")

    print("\n COMIDAS (1 a 5)")
    for i in range(1, 6):
        nome, preco = cardapio[i]
        print(f"{i} - {nome} | R$ {preco}")

    print("\n BEBIDAS (6 a 10)")
    for i in range(6, 11):
        nome, preco = cardapio[i]
        print(f"{i} - {nome} | R$ {preco}")

    print("\n SOBREMESAS (11 a 15)")
    for i in range(11, 16):
        nome, preco = cardapio[i]
        print(f"{i} - {nome} | R$ {preco}")

    print("\n==============================")

def fazer_pedido():
    total = 0

    while True:
        mostrar_cardapio()

        print("\n1 - Adicionar algo ao pedido")
        print("2 - Remover algo do pedido")
        print("3 - Finalizar o pedido")

        opção = ler_numero("Escolha: ")

        if opção == 1:
            codigo = ler_numero("Código do produto: ")
            if codigo in cardapio:
                pedido.append(codigo)
                print("Item adicionado!")
            else:
                print("Código inválido!")

        elif opção == 2:
            codigo = ler_numero("Código para remover: ")
            if codigo in pedido:
                pedido.remove(codigo)
                print("Item removido!")
            else:
                print("Item não está no pedido!")

        elif opção == 3:
            for item in pedido:
                total += cardapio[item][1]

            print("\nTotal da compra: R$", total)
            pedido.clear()
            break

        else:
            print("Opção inválida!")


def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Fazer cadastro")
        print("2 - Ver o cardápio")
        print("3 - Sair do cardápio")

        opção = ler_numero("Escolha: ")

        if opção == 1:
            cadastro()
        elif opção == 2:
            fazer_pedido()
        elif opção == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


print("=== Cardápio Acessível ===")

audio = input("Ativar áudio do cardápio? (s/n): ")

menu()