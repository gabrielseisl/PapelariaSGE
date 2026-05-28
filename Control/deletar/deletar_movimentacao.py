import mysql.connector
from conexao import conectar

def deletar_movimentacao():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_movimentacao = input("Digite o ID da movimentacao que deseja deletar: ")
        cursor.execute("DELETE FROM movimentacao WHERE  id_movimentacao = %s", (id_movimentacao,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Movimentação{ id_movimentacao} deletada com sucesso!")
        else:
            print(f"Nenhuma movimentação encontrada com ID { id_movimentacao}.")

        cursor.close()
        conexao.close()