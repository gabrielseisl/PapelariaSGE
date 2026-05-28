import mysql.connector
from conexao import conectar

def deletar_categoria():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_categoria = input("Digite o ID da categoria que deseja deletar: ")
        cursor.execute("DELETE FROM categoria WHERE id_categoria  = %s", (id_categoria,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Estoque cd{id_categoria } deletado com sucesso!")
        else:
            print(f"Nenhum estoque cd encontrado com ID {id_categoria }.")

        cursor.close()
        conexao.close()