import Controller
import os.path

def criarArquivos(*nome):
    for nomeArquivo in nome:
        if not os.path.exists(nomeArquivo):
            with open(nomeArquivo) as arq:
                arq.write("")

criarArquivos("categoria.txt", "clientes.txt", "estoque.txt", "fornecedores.txt", "funcionarios.txt", "venda.txt")

if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar ( Categorias )\n"
                          "Digite 2 para acessar ( Estoque )\n"
                          "Digite 3 para acessar ( Fornecedor )\n"
                          "Digite 4 para acessar ( Cliente )\n"
                          "Digite 5 para acessar ( Funcionario )\n"
                          "Digite 6 para acessar ( Vendas )\n"
                          "Digite 7 para ver os produtos mais vendidos\n"
                          "Digite 8 para sair\n"
                          ))
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar uma categorias\n"
                                    "Digite 2 para remover uma categorias\n"
                                    "Digite 3 para alterar uma categorias\n"
                                    "Digite 4 para mostrar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"
                                    ))
                if decidir == 1:
                    categoria = input("Digite a categoria que deseja cadastrar\n")
                    cat.cadastrarCategoria(categoria)
                elif decidir == 2:
                    categoria = input("Digite a categoria que deseja remover\n")
                    cat.removerCategoria(categoria)
                elif decidir ==3:
                    categoria = input("Digite a categoria que deseja alterar\n")
                    nova_categoria = input("Digite a categoria para qual deseja alterar\n")
                    cat.alterarCategoria(categoria, nova_categoria)
                elif decidir==  4:
                    cat.mostrarCategorias()
                else:
                    break
        
        if local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para mver o estoque\n"
                                    "Digite 5 para sair\n"
                                    ))
                if decidir == 1:
                    nome = input("Digite um nome do produto que deseja cadastrar\n")
                    preco = input("Digite o preço do produto que deseja cadastrar\n")
                    categoria = input("Digite a categoria do produto que deseja cadastrar\n")
                    quantidade = input("Digite a quantidade do produto que deseja cadastrar\n")
                    cat.cadastrarProduto(nome, preco, categoria, quantidade)
                elif decidir == 2:
                    produto = input("Digite um produto que deseja remover\n")
                    cat.
                elif decidir ==3:
                    categoria = input("Digite um produto que deseja alterar\n")
                    nova_categoria = input("Digite um produto para qual deseja alterar\n")
                    cat.alterar_categoria(categoria, nova_categoria)
                elif decidir==  4:
                    cat.mostrar_categoria()
                else:
                    break
