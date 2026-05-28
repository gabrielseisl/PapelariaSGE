import mysql.connector
from conexao import conectar

def deletar_loja():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_loja = input("Digite o ID daloja que deseja deletar: ")
        cursor.execute("DELETE FROM loja WHERE id_loja  = %s", (id_loja,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Loja {id_loja } deletado com sucesso!")
        else:
            print(f"Nenhuma loja encontrada com ID {id_loja }.")

        cursor.close()
        conexao.close()