usuario_logado = None

def definir(usuario):
    global usuario_logado
    usuario_logado = usuario

def usuario_mudou():
    return usuario_logado