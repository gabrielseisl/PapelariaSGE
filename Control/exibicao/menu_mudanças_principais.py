from exibicao.menu_ver_trigger import ver_mudanças
from exibicao.menu_inserir_trigger import inserir_trigger
def menu_mudanças():

    while True:
        print("=======MUDANÇAS======")
        print("1-Fazer mudanças")
        print("2-Ver mudanças")
        print("0-Retorno")
        opcao=input("O que vai querer fazer? ")

        if opcao=="1":
            inserir_trigger()
        
        elif opcao =="2":
            ver_mudanças()

        elif opcao == "0":
            return
        else:
            
            print("Opção inválida 👎")
