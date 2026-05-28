import mysql.connector
from conexao import conectar

def deletar_fornecedor():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_fornecedor = input("Digite o ID do fornecedor que deseja deletar: ")
        cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = %s", (id_fornecedor,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Fornecedor {id_fornecedor} deletado com sucesso!")
        else:
            print(f"Nenhum fornecedor encontrado com ID {id_fornecedor}.")

        cursor.close()
        conexao.close()