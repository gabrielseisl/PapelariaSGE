from senha.tela_inicial import tela_inicial
from exibicao.menu_principal import menu_principal
from conexao import conectar
import sessaobadass

usuario = tela_inicial()

if not usuario:
    exit()

sessaobadass.definir(usuario)

conexao = conectar()


menu_principal()