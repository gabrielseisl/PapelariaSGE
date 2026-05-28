from senha.usuarios import carregar, salvar
from senha.censura import censura

def cadastro():
    usuarios = carregar()

    print("\n-- Cadastro --")
    usuario = input("Usuario: ")

    if not usuario:
        print("Nome invalido.")
        return False

    # Censura o nome do usuário
    usuario_censurado = censura(usuario)

    # Verifica se o usuário já existe
    if usuario_censurado in usuarios:
        print("Usuario ja existe.")
        return False

    senha = input("Senha: ")
    confirma = input("Confirma senha: ")

    if senha != confirma:
        print("Senhas diferentes.")
        return False

    # Salva usuario e senha censurados
    usuarios[usuario_censurado] = censura(senha)

    salvar(usuarios)

    print(f"Cadastro feito com sucesso, {usuario}.")
    return True