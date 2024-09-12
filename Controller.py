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

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y') 
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y') 
        vendasFiltradas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1 
                                      and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas)) 
        
        cont =1
        total =0
        for i in vendasFiltradas:
            print(f'==========Venda [{cont}]===============')
            print(f"Nome: {i.itensVendido.nome}\n"
                  f"Categoria: {i.itensVendido.categoria}\n"
                  f"Data: {i.data}\n"
                  f"Quantidade: {i.quantidadeVendida}\n"
                  f"Cliente: {i.comprador}\n"
                  f"Vendedor: {i.vendedor}\n")
            cont+=1
            total+=int(i.itensVendido.preco) * int(i.quantidadeVendida)
        print(f"total vendido: {total}")


class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x=DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.cnpj == cnpj, x)) 

        if len(listaCnpj) > 0:
            print("cnpj ja existe")
        elif len(listaTelefone) > 0:
            print("telefone ja existe")
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print("cnpj ou telefone invalido")

    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novoCategoria):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCnpj, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novoCategoria)
                         if x.nome == nomeAlterar else (x), x))
            else:
                print("cnpj ja existe")
        else:
            print("fornecedor nao encontrado")

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.write(f'{i.nome}|{i.cnpj}|{i.telefone}|'+str(i.categoria)+'\n')
            print("fornecedor alterado com sucesso")

    def removerFornecedor(self, nome):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("fornecedor nao encontrado")
            return None
        
        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.write(f'{i.nome}|{i.cnpj}|{i.telefone}|'+str(i.categoria)+'\n')
            print("fornecedor removido co sucesso")

    def mostrarFornecedores(self):

        fornecedores = DaoFornecedor.ler()

        if len(fornecedores) == 0:
            print("Nenhum fornecedor encontrado")

        for i in fornecedores:
            print(f'==========Fornecedores===============')
            print(f"Categoria: {i.categoria}\n"
                f"Nome: {i.nome}\n"
                f"Telefone: {i.telefone}\n"
                f"EndereCNPJço: {i.cnpj}\n")
            

class ControllerCategoria:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print("categoria cadastrada com sucesso")
        else:
            print('A categoria que deseja cadastrar ja existe')

    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print('A alteração foi efetuada com sucesso')
        else:
            print("nome nao encontrado")

        with open('categorias.txt', 'w') as arq:
            for i in x:
                arq.write(f'{i.categoria}\n')
        
            print('Cliente alterado com sucesso')

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        if len(cat) <= 0:
            print("categoria nao encontrada")
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')
            #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE
            with open('categorias.txt', 'w') as arq:
                for i in x:
                    arq.write(f'{i.categoria}\n')

    def alterarCategoria(self, categoriarAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriarAlterar, x))
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriarAlterar) 
                             else (x), x))


class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x=DaoPessoa.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) >0:
            print("cpf ja existe")
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente cadastrado com sucesso!')
            else:
                print('Telefone ou cpf invalido')

    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                         if x.nome == nomeAlterar else (x), x))
        else:
            print("nome nao encontrado")

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.write(f'{i.nome}|{i.telefone}|{i.cpf}|{i.email}|{i.endereco}\n')
        
            print('Cliente alterado com sucesso')

    def removerCliente(self, nome):
        x = DaoPessoa.ler()
        cat = list(filter(lambda x: x.nome == nome, x))
        if len(cat) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("categoria nao encontrada")
            return None
        
        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.write(f'{i.nome}|{i.cnpj}|{i.telefone}|{i.cpf}|{i.email}|{i.endereco}\n')
            
            print('Cliente removido com sucesso')

    def mostrarCliente(self):
        clientes = DaoPessoa.ler()

        if len(clientes) == 0:
            print("Nenhum cliente encontrado")

        for i in clientes:
            print(f'==========Cliente===============')
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Email: {i.email}\n"
                  f"Endereço: {i.endereco}\n"
                  f"CPF: {i.cpf}\n")


class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))
        if len(listaCpf) >0:
            print("cpf ja existe")
        elif len(listaClt) >0:
            print("Ja existe um funcionario com essa clt")
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionario cadastrado com sucesso!')
            else:
                print('Telefone ou cpf invalido')

    def alterarFuncionario(self, nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                         if x.nome == nomeAlterar else (x), x))
        else:
            print("nome nao encontrado")

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.write(f'{i.clt}|{i.nome}|{i.telefone}|{i.cpf}|{i.email}|{i.endereco}\n')
        
            print('Funcionario alterado com sucesso')

    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()
        

        est = list(filter(lambda x: x.nome ==nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome: 
                    del x[i]
                    break
        else:
            print("Funcionario não encontrado")
            return None

        with open('funcionario.txt', 'w') as arq:
            for i in x:
                arq.write(f"{i.nome}|{i.telefone}|{i.cpf}|{i.email},{i.endereco}\n")

            print('funcionario removido com sucesso!')

    def mostrarFuncionario(self):
        funcionario = DaoFuncionario.ler()

        if len(funcionario) == 0:
            print("Nenhum funcionario encontrado")

        for i in funcionario:
            print(f'==========Funcionario===============')
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Email: {i.email}\n"
                  f"Endereço: {i.endereco}\n"
                  f"CPF: {i.cpf}\n"
                  f"CLT: {i.clt}\n")

    




a = ControllerVenda()
a.mostrarVenda("05/09/2024", "09/09/2024")



# a = ControllerVenda()
# a.cadastrarVenda('maca', 'joão', 'caio', 1)


# a = ControllerEstoque()
# a.cadastrarProduto('maca',10,'Frutas',5)