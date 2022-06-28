from estoque import *

class Produto:
    def __init__(self):
        self.listaProduto = []
        
    def salvar_produtos(self):
        entrada_cod = input('Informe o código: ')
        entrada_descrição = input('Informe a descrição: ')
        entrada_fabricante = input('Informe a fabricante: ')
        entrada_quantidade = input('Informe a quantidade: ')
        self.listaProduto.append(Estoque(entrada_cod, entrada_descrição, entrada_fabricante, entrada_quantidade))
        print('Cadrasto de produtos feito com sucesso!')
        print('===================================')

    def listar_todos_produtos(self):
        for i in range(len(self.listaProduto)):
            print('Cod:',self.listaProduto[i].cod,'Produtos:',self.listaProduto[i].descrição, 'Código:',self.listaProduto[i].cod)
            print('===================================')

    def alterar_descrição(self):
        entrada = input('Digite o código do produto: ')
        for i in range(len(self.listaProduto)):
            if entrada == self.listaProduto[i].descrição:
                self.listaProduto[i].descrição = input('Digite a nova descrição: ')
                print('Descrição alterada com sucesso!')
                print('===================================')


    def procurar_produtos(self):
        entrada = input('digite qual produto quer procurar: ')
        for i in range(len(self.listaProduto)):
            if entrada == self.listaProduto[i].cod:
                self.listaProduto[i].produto = input('Produtos')            