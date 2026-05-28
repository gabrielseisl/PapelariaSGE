from senha.salvamento import cadastro
from senha.login import login

def tela_inicial():

    while True:

        print("\nPAPELARIA SGE")
        print("1 - Entrar")
        print("2 - Criar conta")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":

            usuario = login()

            if usuario:
                return usuario

        elif opcao == "2":
            cadastro()

        elif opcao == "0":
            print("Sistema encerrado 👋")
            break

        else:
            print("Opcao invalida.")