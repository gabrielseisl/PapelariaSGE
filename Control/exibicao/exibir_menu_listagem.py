from exibicao.exibir_fabricante import exibir_dados_fabricante
from exibicao.exibir_produto import exibir_dados_produto
from exibicao.exibir_fornecedor import exibir_dados_fornecedor
from exibicao.exibir_pedido import exibir_dados_pedido
from exibicao.exibir_estoque_cd import exibir_dados_estoque_cd
from exibicao.exibir_loja import exibir_dados_loja
from exibicao.exibir_estoque_loja import exibir_dados_estoque_loja
from exibicao.exibir_categoria import exibir_dados_estoque_categoria
from exibicao.exibir_movimentacao import exibir_dados_movimentacao
from exibicao.exibir_venda import exibir_vendas



def menu_listagem():

    exibir_menu = True

    while True:

        if exibir_menu:
            print("\n========== LISTAGENS ==========")
            print("1  - Listar Fabricantes🏭")
            print("2  - Listar Produtos📦")
            print("3  - Listar Fornecedores🤝")
            print("4  - Listar Pedidos📋")
            print("5  - Listar Estoque CD🛒")
            print("6  - Listar Lojas🛍️")
            print("7  - Listar Estoque Loja💲")
            print("8  - Listar Categorias🗂️")
            print("9  - Listar Movimentações🚚")
            print("10 - Listar Vendas💸")
            print("\n0 - Voltar 🔙")
            exibir_menu = False

        opcao = input("\nEscolha uma opção (ou '11' para ver o menu): ")

        if opcao == "1":
            exibir_dados_fabricante()

        elif opcao == "2":
            exibir_dados_produto()

        elif opcao == "3":
            exibir_dados_fornecedor()

        elif opcao == "4":
            exibir_dados_pedido()

        elif opcao == "5":
            exibir_dados_estoque_cd()

        elif opcao == "6":
            exibir_dados_loja()

        elif opcao == "7":
            exibir_dados_estoque_loja()

        elif opcao == "8":
            exibir_dados_estoque_categoria()

        elif opcao == "9":
            exibir_dados_movimentacao()

        elif opcao == "10":
            exibir_vendas()

        elif opcao == "11":
            exibir_menu = True
            

        elif opcao == "0":
            return

        else:
            print("Opção inválida 👎")