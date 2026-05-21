import mysql.connector
from conexao import conectar

from cadastro.cadastro_fabricante import inserir_dados_fabricante
from exibicao.exibir_fabricante import exibir_dados_fabricante


from cadastro.cadastro_produto import inserir_dados_produto
from exibicao.exibir_produto import exibir_dados_produto


from cadastro.cadastro_fornecedor import inserir_dados_fornecedor
from exibicao.exibir_fornecedor import exibir_dados_fornecedor


from cadastro.cadastro_pedido import inserir_dados_pedido
from exibicao.exibir_pedido import exibir_dados_pedido


from cadastro.cadastro_estoque_cd import inserir_dados_estoque_cd
from exibicao.exibir_estoque_cd import exibir_dados_estoque_cd


from cadastro.cadastro_loja import inserir_dados_loja
from exibicao.exibir_loja import exibir_dados_loja


from cadastro.cadastro_estoque_loja import inserir_dados_estoque_loja
from exibicao.exibir_estoque_loja import exibir_dados_estoque_loja


from cadastro.cadastro_categoria import inserir_dados_categoria
from exibicao.exibir_categoria import exibir_dados_estoque_categoria


from cadastro.cadastro_movimentacao import inserir_dados_movimentacao
from exibicao.exibir_movimentacao import exibir_dados_movimentacao


from cadastro.cadastro_venda import inserir_dados_vendas
from exibicao.exibir_venda import exibir_vendas


from exibicao.exibir_trigger import exibir_logs_estoque


while True:
    conexao = conectar()

    print("\n========== PAPELARIA SGE ==========")
    print("\nBem Vindo(a) Ao Sistema 💻")

    print("\n=========== CADASTRAR ===========")
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

    print("\n============ LISTAR ============")
    print("11 - Listar Fabricantes🏭")
    print("12 - Listar Produtos📦")
    print("13 - Listar Fornecedores🤝")
    print("14 - Listar Pedidos📋")
    print("15 - Listar Estoque CD🛒")
    print("16 - Listar Lojas🛍️")
    print("17 - Listar Estoque Loja💲")
    print("18 - Listar Categorias🗂️")
    print("19 - Listar Movimentações🚚")
    print("20 - Listar Vendas💸")
    print("21 - Listar Mudanças Estoque CD🔄")

    print("\n0 - Sair❌")

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

    elif opcao == "11":
        exibir_dados_fabricante()

    elif opcao == "12":
        exibir_dados_produto()

    elif opcao == "13":
        exibir_dados_fornecedor()

    elif opcao == "14":
        exibir_dados_pedido()

    elif opcao == "15":
        exibir_dados_estoque_cd()

    elif opcao == "16":
        exibir_dados_loja()

    elif opcao == "17":
        exibir_dados_estoque_loja()

    elif opcao == "18":
        exibir_dados_estoque_categoria()

    elif opcao == "19":
        exibir_dados_movimentacao()

    elif opcao == "20":
        exibir_vendas()

    elif opcao == "21":
        exibir_logs_estoque()

    elif opcao == "0":
        print("Sistema encerrado 👋")
        break

    else:
        print("Opção inválida 👎")


