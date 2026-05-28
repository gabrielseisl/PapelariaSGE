from cadastro.inserir_trigger_estoquecd import inserir_log_estoque_cd
from cadastro.inserir_trigger_estoqueloja import inserir_log_estoque_loja
from cadastro.inserir_trigger_loja import inserir_log_loja
from cadastro.inserir_trigger_movimentacao import inserir_log_movimentacao
from cadastro.inserir_trigger_pedido import inserir_log_pedido
from cadastro.inserir_trigger_produto import inserir_log_produto
from cadastro.inserir_trigger_venda import inserir_log_venda


def inserir_trigger():
    while True:
            print("========Mudanças=========")
            print("1 -  Colocar Produtos📦")
            print("2  - Colocar Pedidos📋")
            print("3  - Colocar Estoque CD🛒")
            print("4 -  Colocar Lojas🛍️")
            print("5 -  Colocar Estoque Loja💲")
            print("6  - Colocar Movimentações🚚")
            print("7  - Colocar Vendas💸")
            print("\n0 - Voltar 🔙")
            opcao=input("O que vai querer mudar? ")
                    
            if opcao == "1":
                 inserir_log_produto()
                    
                    
            elif opcao == "2":
                 inserir_log_pedido()
                    
            elif opcao == "3":
                inserir_log_estoque_cd()

            elif opcao == "4":
                 inserir_log_loja()
                    
            elif opcao == "5":
                 inserir_log_estoque_loja()
                
        
                    
            elif opcao == "6":
                 inserir_log_movimentacao()
                    
            elif opcao == "7":
                 inserir_log_venda()
                    
            elif opcao == "0":
                return 
                    