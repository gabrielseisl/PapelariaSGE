import mysql.connector
from conexao import conectar

def deletar_produto():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_produto = input("Digite o ID do produto que deseja deletar: ")
        cursor.execute("DELETE FROM produto WHERE id_produto = %s", (id_produto,))
        conexao.commit()
        # rowcount retorna quantas linhas foram afetadas pelo DELETE
        # se for maior que 0, significa que encontrou e deletou o registro
        # se for 0, significa que não achou nenhum registro com esse ID
        if cursor.rowcount > 0:
            print(f"Produto {id_produto} deletado com sucesso!")
        else:
            print(f"Nenhum produto encontrado com ID {id_produto}.")

        cursor.close()
        conexao.close()