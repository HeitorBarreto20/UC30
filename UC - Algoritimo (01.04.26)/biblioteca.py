#Dicionário para armazenar os livros
catalogo = {}

#Dicionario para armazenar os empréstimos ativos
EmprestimosAtivos = {}

#Função: Adicionar livro
def AdicionarLivro (codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print (f"Erro: Livro com código {codigo} já existe!")
        return False

    catalogo [codigo] = {
    "titulo": titulo,
    "autor": autor,
    "quantidade": quantidade
}
    print (f"Livro ´{titulo}´ adicionado com sucesso!")
    return True

AdicionarLivro ("L001", "Código Limpo", "Robert Martin", 2)

# Função: Devolver livro
def DevolverLivro(codigo):
    if codigo not in EmprestimosAtivos:
        print(f"Erro: Nenhum empréstimo encontrado para o código {codigo}!")
        return False

    # Recupera dados do empréstimo
    quantidade_emprestada = EmprestimosAtivos[codigo]

    # Devolve ao catálogo
    catalogo[codigo]["quantidade"] += quantidade_emprestada

    # Remove dos empréstimos ativos
    del EmprestimosAtivos[codigo]

    print(f"Livro '{catalogo[codigo]['titulo']}' devolvido com sucesso!")
    return True