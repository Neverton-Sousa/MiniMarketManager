from Models import*

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt','a') as arq:
            arq.write(f'{categoria}\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt','r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n',''), cls.categoria))

        cat=[Categoria(i) for i in cls.categoria]
        # for i in cls.categoria:
        #     cat.append(Categoria(i))

        return cat

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt','a') as arq:
            arq.write(f'{venda.itensVendido.nome}|{venda.itensVendido.preco}|{venda.itensVendido.categoria}|{venda.vendedor}|{venda.comprador}|{venda.quantidadeVendida}|{venda.data}\n')
            
    @classmethod
    def ler(cls):
        with open('venda.txt','r') as arq:
            cls.venda = arq.readlines()
    
        cls.venda = list(map(lambda x: x.replace('\n',''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))

        vend=[Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]) for i in cls.venda]
        # for i in cls.venda:
        #     vend.append(Venda(Produtos(i[0],i[1],i[2]),i[3],i[4],i[5]))

        return vend

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt','a') as arq:
            arq.write(f'{produto.nome}|{produto.preco}|{produto.categoria}|{quantidade}\n')
            
    @classmethod
    def ler(cls):
        with open('estoque.txt','r') as arq:
            cls.estoque = arq.readlines()
    
        cls.estoque = list(map(lambda x: x.replace('\n',''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
    
        est=[Estoque(Produtos(i[0], i[1], i[2]), int(i[3]))  for i in cls.estoque if len(cls.estoque) > 0]
        return est
    
class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedores.txt','a') as arq:
            arq.write(f'{fornecedor.nome}|{fornecedor.cnpj}|{fornecedor.contato}|{fornecedor.categoria}\n')
            
    @classmethod
    def ler(cls):
        with open('fornecedores.txt','r') as arq:
            cls.fornecedores = arq.readlines()
    
        cls.fornecedores = list(map(lambda x: x.replace('\n',''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))

        forn=[Fornecedor(i[0], i[1], i[2], i[3])  for i in cls.fornecedores]
        return forn
    
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('clientes.txt','a') as arq:
            arq.write(f'{pessoa.nome}|{pessoa.telefone}|{pessoa.cpf}|{pessoa.email}|{pessoa.endereco}\n')
            
    @classmethod
    def ler(cls):
        with open('clientes.txt','r') as arq:
            cls.clientes = arq.readlines()
    
        cls.clientes = list(map(lambda x: x.replace('\n',''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        clientes=[Pessoa(i[0], i[1], i[2], i[3], i[4])  for i in cls.clientes]
        return clientes


class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt','a') as arq:
            arq.write(f'{funcionario.clt}|{funcionario.nome}|{funcionario.telefone}|{funcionario.cpf}|{funcionario.email}|{funcionario.endereco}\n')
            
    @classmethod
    def ler(cls):
        with open('funcionarios.txt','r') as arq:
            cls.funcionarios = arq.readlines()
    
        cls.funcionarios = list(map(lambda x: x.replace('\n',''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

        funcionario=[Funcionario(i[0], i[1], i[2], i[3], i[4], i[5])  for i in cls.funcionarios]
        return funcionario

