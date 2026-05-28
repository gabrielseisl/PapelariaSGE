import mysql.connector
from conexao import conectar

def deletar_estoque_cd():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_estoque_cd = input("Digite o ID do estoque cd que deseja deletar: ")
        cursor.execute("DELETE FROM estoque_cd WHERE id_estoque_cd = %s", (id_estoque_cd,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Estoque cd{id_estoque_cd} deletado com sucesso!")
        else:
            print(f"Nenhum estoque cd encontrado com ID {id_estoque_cd}.")

        cursor.close()
        conexao.close()