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
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    print("Cadastro realizado!\n")

def mostrar_cardapio():
    print("\n========== CARDÁPIO ==========")

    print("\n COMIDAS (1 a 5)")
    print("----------------------")
    for i in range(1, 6):
        nome, preco = cardapio[i]
        print(f"{i} - {nome} | R$ {preco}")

    print("\n BEBIDAS (6 a 10)")
    print("----------------------")
    for i in range(6, 11):
        nome, preco = cardapio[i]
        print(f"{i} - {nome} | R$ {preco}")

    print("\n SOBREMESAS (11 a 15)")
    print("----------------------")
    for i in range(11, 16):
        nome, preco = cardapio[i]
        print(f"{i} - {nome} | R$ {preco}")

    print("\n==============================")

def fazer_pedido():
    total = 0

    while True:
        mostrar_cardapio()

        print("\n1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Finalizar pedido")

        op = ler_numero("Escolha: ")

        if op == 1:
            cod = ler_numero("Código do produto: ")
            if cod in cardapio:
                pedido.append(cod)
                print("Item adicionado!")
            else:
                print("Código inválido!")

        elif op == 2:
            cod = ler_numero("Código para remover: ")
            if cod in pedido:
                pedido.remove(cod)
                print("Item removido!")
            else:
                print("Item não está no pedido!")

        elif op == 3:
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
        print("1 - Cadastro")
        print("2 - Ver Cardápio")
        print("3 - Sair")

        op = ler_numero("Escolha: ")

        if op == 1:
            cadastro()
        elif op == 2:
            fazer_pedido()
        elif op == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


print("=== Cardápio Acessível ===")

audio = input("Ativar áudio? (s/n): ")

menu()