from cadastro.cadastro_fabricante import inserir_dados_fabricante
from cadastro.cadastro_produto import inserir_dados_produto
from cadastro.cadastro_fornecedor import inserir_dados_fornecedor
from cadastro.cadastro_pedido import inserir_dados_pedido
from cadastro.cadastro_estoque_cd import inserir_dados_estoque_cd
from cadastro.cadastro_loja import inserir_dados_loja
from cadastro.cadastro_estoque_loja import inserir_dados_estoque_loja
from cadastro.cadastro_categoria import inserir_dados_categoria
from cadastro.cadastro_movimentacao import inserir_dados_movimentacao
from cadastro.cadastro_venda import inserir_dados_vendas


def menu_cadastro():

    while True:

        print("\n========== CADASTROS ==========")

        print("1  - Cadastrar Fabricante🏭")
        print("2  - Cadastrar Produto📦")
        print("3  - Cadastrar Fornecedor🤝")
        print("4  - Cadastrar Pedido📋")
        print("5  - Cadastrar Estoque CD🛒")
        print("6  - Cadastrar Loja🛍️")
        print("7  - Cadastrar Estoque Loja💲")
        print("8  - Cadastrar Categoria🗂️")
        print("9  - Cadastrar Movimentação🚚")
        print("10 - Cadastrar Venda💸")

        print("\n0 - Voltar 🔙")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            inserir_dados_fabricante()

        elif opcao == "2":

            inserir_dados_produto()

        elif opcao == "3":

            inserir_dados_fornecedor()

        elif opcao == "4":

            inserir_dados_pedido()

        elif opcao == "5":

            inserir_dados_estoque_cd()

        elif opcao == "6":

            inserir_dados_loja()

        elif opcao == "7":

            inserir_dados_estoque_loja()

        elif opcao == "8":

            inserir_dados_categoria()

        elif opcao == "9":

            inserir_dados_movimentacao()

        elif opcao == "10":

            inserir_dados_vendas()

        elif opcao == "0":

            return

        else:

            print("Opção inválida 👎")