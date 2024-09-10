from Models import Categoria,  Estoque, Produtos, Fornecedor, Pessoa, Funcionario, Venda
from DAO import DaoCategoria, DaoVenda, DaoEstoque, DaoFornecedor, DaoPessoa, DaoFuncionario
from datetime import datetime

class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
            
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('categoria cadastrada com sucesso')
        else:
            print('categoria ja existe')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <=0:
            print('categoria não existe')
        else:
            # DaoCategoria.deletar(categoriaRemover)
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('categoria removida com sucesso')
        #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.write(f'{i.categoria}\n')
                    
    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x) , x))
                print("operação efetuada com sucesso!")
                #TODO: ALTERAR A CATEGORIA TAMBEM NO ESTOQUE
            else:
                print("A acategoria para qual deseja alterar já existe")
        else:
            print("A acategoria para qual deseja alterar não existe")
        
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.write(f'{i.categoria}\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Nenhuma categoria foi cadastrada')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto == nome, x))

        if len(h)> 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('produto cadastrado com sucesso')
            else:
                print('produto já existe em estoque')
        else:
            print('categoria inexistente')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Nenhum produto foi cadastrado')
        else:
            for i in estoque:
                print(f"Nome: {i.produto.nome}\n"
                      f"Preco: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}\n")


class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp=[]
        exist= False
        quantidade = False
        for i in x:
            if not exist:
                if i.produto.nome == nomeProduto:
                    exist = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int (quantidadeVendida)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.preco), vendedor, comprador, quantidadeVendida)

                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)
            temp.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))   

        arq = open('estoque.txt', 'w')
        arq.write("")

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.write(f"{i.produto.nome}|{i.produto.preco}|{i.produto.categoria}|{str(i.quantidade)}\n")
        
        if exist == False:
            print("O produto não existe")
            return None
        elif not quantidade:
            print("A quantidade vendida não contem em estoque")
        else:
            print("Venda realizada com sucesso")
            return valorCompra

    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos=[]
        for i in vendas:
            nome = i.itensVendido.nome 
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                                if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})

        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

        print('esses são os produtos mais vendidos')
        a=1
        for i in ordenado:
            print(f'==========Produto [{a}]===============')
            print(f"Produto: {i['produto']}\n"
                    f"Quantidade: {i['quantidade']}\n")
            a+=1


a = ControllerVenda()
a.relatorioProdutos()
# a = ControllerVenda()
# a.cadastrarVenda('maca', 'joão', 'caio', 1)


# a = ControllerEstoque()
# a.cadastrarProduto('maca',10,'Frutas',5)