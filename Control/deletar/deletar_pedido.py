import mysql.connector
from conexao import conectar

def deletar_pedido():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_pedido = input("Digite o ID do pedido que deseja deletar: ")
        cursor.execute("DELETE FROM pedido WHERE id_pedido = %s", (id_pedido,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Pedido {id_pedido} deletado com sucesso!")
        else:
            print(f"Nenhum pedido encontrado com ID {id_pedido}.")

        cursor.close()
        conexao.close()