from deletar.deletar_fabricantes import deletar_fabricante
from deletar.deletar_categoria import deletar_categoria
from deletar.deletar_estoque_cd import deletar_estoque_cd
from deletar.deletar_estoque_loja import  deletar_estoque_loja
from deletar.deletar_fornecedor import  deletar_fornecedor
from deletar.deletar_loja import deletar_loja
from deletar.deletar_movimentacao import deletar_movimentacao
from deletar.deletar_venda import deletar_venda
from deletar.deletar_produto import deletar_produto
from deletar.deletar_pedido import deletar_pedido

def menu_delete():

    while True:

        print("\n==========Deletar==========")

        print("1  - Deletar Fabricante🏭")
        print("2  - Deletar Produto📦")
        print("3  - Deletar Fornecedor🤝")
        print("4  - Deletar Pedido📋")
        print("5  - Deletar Estoque CD🛒")
        print("6  - Deletar Loja🛍️")
        print("7  - Deletar Estoque Loja💲")
        print("8  - Deletar Categoria🗂️")
        print("9  - Deletar Movimentação🚚")
        print("10 - Deletar Venda💸")

        print("\n0 - Voltar 🔙")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            deletar_fabricante()

        elif opcao == "2":

            deletar_produto()

        elif opcao == "3":

             deletar_fornecedor()

        elif opcao == "4":

            deletar_pedido()

        elif opcao == "5":

            deletar_estoque_cd()

        elif opcao == "6":

            deletar_loja()

        elif opcao == "7":

            deletar_estoque_loja()

        elif opcao == "8":

          deletar_categoria()

        elif opcao == "9":

            deletar_movimentacao()

        elif opcao == "10":

            deletar_venda()

        elif opcao == "0":

            return

        else:

            print("Opção inválida 👎")