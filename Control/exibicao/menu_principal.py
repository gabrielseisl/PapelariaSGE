from exibicao.exibir_menu_cadastro import menu_cadastro
from exibicao.exibir_menu_listagem import menu_listagem
from exibicao.menu_mudanças_principais import menu_mudanças
from exibicao.menu_joins import ver_joins
from exibicao.menu_delete import menu_delete

def menu_principal():

    while True:

        print("\n======= PAPELARIA SGE =======")
        print("1 - Acessar Sistema De Cadastros 💻")
        print("2 - Acessar Sistema De Listagens📋")
        print("3 - Acessar Mudanças🔄")
        print("4 - Ver Informações Mescladas")
        print("5-  Deletar Dados")
        print("0 - Sair ❌")

        opcao = input("\nEscolha: ")

        if opcao == "1":

            menu_cadastro()

        elif opcao == "2":

            menu_listagem()

        elif opcao == "3":

            menu_mudanças()

        elif opcao == "4":

            ver_joins()

        elif opcao == "5":

            menu_delete()

        elif opcao == "0":

            print("Sistema encerrado 👋")
            break

        else:

            print("Opção inválida 👎")
        

        