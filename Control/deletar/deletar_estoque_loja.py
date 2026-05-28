import mysql.connector
from conexao import conectar

def deletar_estoque_loja():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_estoque_loja = input("Digite o ID do estoque loja que deseja deletar: ")
        cursor.execute("DELETE FROM estoque_loja WHERE id_estoque_loja = %s", (id_estoque_loja,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Estoque loja {id_estoque_loja} deletado com sucesso!")
        else:
            print(f"Nenhum estoque loja encontrado com ID {id_estoque_loja}.")

        cursor.close()
        conexao.close()