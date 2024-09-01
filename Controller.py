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
            else:
                print("A acategoria para qual deseja alterar já existe")
        else:
            print("A acategoria para qual deseja alterar não existe")
        
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.write(f'{i.categoria}\n')
                print('awdtg')


a = ControllerCategoria()
a.alterarCategoria('Verduras', 'Carnes')