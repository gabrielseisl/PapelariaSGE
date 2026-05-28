from exibicao.exibir_trigger_estoque_loja import exibir_logs_estoque_loja
from exibicao.exibir_trigger_estoquecd import exibir_logs_estoque_cd
from exibicao.exibir_trigger_loja import exibir_logs_loja
from exibicao.exibir_trigger_pedido import exibir_logs_pedido
from exibicao.exibir_trigger_venda import exibir_logs_venda
from exibicao.exibir_trigger_produto import exibir_logs_produto

def ver_mudanças():
    while True:
            print("========Mudanças=========")
            print("1  - Ver Produtos📦")
            print("2  - Ver Pedidos📋")
            print("3  - Ver Estoque CD🛒")
            print("4  - Ver Lojas🛍️")
            print("5  - Ver Estoque Loja💲")
            print("6 - Ver Vendas💸")
            print("\n0 - Voltar 🔙")
            opcao=input("O que vai querer ver? ")
            if opcao == "1":
                exibir_logs_produto()
            elif opcao == "2":
                exibir_logs_pedido()
            elif opcao == "3":
                exibir_logs_estoque_cd()
            elif opcao == "4":
                exibir_logs_loja()
            elif opcao == "5":
                exibir_logs_estoque_loja()
            elif opcao == "6":
                exibir_logs_venda()
            elif opcao == "0":
                return 
            else:
                print("Opção inválida 👎")
                    
            
                    