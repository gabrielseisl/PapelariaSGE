import mysql.connector
from conexao import conectar

def deletar_fabricante():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_fabricante = input("Digite o ID do fabricante que deseja deletar: ")
        cursor.execute("DELETE FROM fabricante WHERE id_fabricante = %s", (id_fabricante,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Fabricante {id_fabricante} deletado com sucesso!")
        else:
            print(f"Nenhum fabricante encontrado com ID {id_fabricante}.")

        cursor.close()
        conexao.close()