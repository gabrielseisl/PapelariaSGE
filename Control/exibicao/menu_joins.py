from exibicao_join.join_fabprod import exibir_join_fabprod
from exibicao_join.join_fornedido import exibir_join_fornedido
from exibicao_join.join_estoloja import exibir_join_estoloja
from exibicao_join.join_movivenda import exibir_join_movivenda

def ver_joins():
    while True:
            print("========Junção=========")
            print("1  - Ver fabricante/produto")
            print("2  - Ver fornecedor/pedido")
            print("3  - Ver estoque Loja/Loja")
            print("4  - Ver movimentação/venda")
            print("0  - Voltar")
            opcao=input("O que vai querer ver? ")
            if opcao == "1":
                exibir_join_fabprod()
            elif opcao == "2":
                exibir_join_fornedido()
            elif opcao == "3":
                exibir_join_estoloja()
            elif opcao == "4":
                exibir_join_movivenda()
            elif opcao == "0":
                return 
            else:
                print("Opção inválida 👎")