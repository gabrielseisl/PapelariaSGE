from senha.usuarios import carregar
from senha.censura import censura

TENTATIVAS = 3

def login():
# Carrega o dicionário de usuários salvos {usuario_hash: senha_hash}
    usuarios = carregar()

 # Se não houver nenhum usuário cadastrado, avisa e sai
    if not usuarios:
        print("Nenhum foi achado, por favor faça seu cadastro.")
        return False

    print("\n-- Login --")

 # Contador de erros de login
    erros = 0

    while erros < TENTATIVAS:

        volta = input("Para voltar clique s, para continuar clique c: ")

        # Volta para tela inicial
        if volta == "s":
            return False

        elif volta != "c":
            print("Opcao invalida.")
            continue

        usuario = input("Usuario: ")
        senha = input("Senha: ")

# Criptografa o usuário digitado para comparar com o que está salvo
        # (o banco guarda tudo em hash, nunca o texto original)
        usuario_censurado = censura(usuario)

# Verifica se o usuário existe E se a senha bate
        if usuario_censurado in usuarios and usuarios[usuario_censurado] == censura(senha):
            print(f"Olá, parabéns {usuario} você acessou!")
            return usuario

 # Se errou, incrementa o contador e avisa quantas tentativas restam
        erros += 1

        if erros < TENTATIVAS:
            print(f"Errou. {TENTATIVAS - erros} tentativa(s) restante(s).")
 # Esgotou as 3 tentativas — bloqueia o acesso
    print("Acesso bloqueado.")
    return False