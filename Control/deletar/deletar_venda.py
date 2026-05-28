import mysql.connector
from conexao import conectar

def deletar_venda():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_venda = input("Digite o ID da venda que deseja deletar: ")
        cursor.execute("DELETE FROM venda WHERE id_venda = %s", (id_venda,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Venda {id_venda} deletada com sucesso!")
        else:
            print(f"Nenhuma venda encontrada com ID {id_venda}.")

        cursor.close()
        conexao.close()