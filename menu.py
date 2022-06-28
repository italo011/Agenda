from produto import Produto
from produto import *

class Menu:
        def __init__(self):
            produto = Produto()

            while True:
                entrada = input ('informe a opção desejada\n1 -Novo Produto (Código) \n2 -Listar Produtos\n3 - Alterar descrição\n4 - Procurar produto\n5 - Sair')
                if entrada == '1':
                    produto.salvar_produtos()
                elif entrada == '2':
                    produto.listar_todos_produtos()
                elif entrada == '3':
                    produto.alterar_descrição()
                elif entrada == '4':
                    produto.procurar_produtos()
                elif entrada == '5':
                    print('saindo')
                    break
                else:
                    print('opção não existente')                