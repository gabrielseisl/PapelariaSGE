import mysql.connector
from conexao import conectar

def exibir_dados_loja():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_loja, nome_loja,endereco,gerente, id_estoque_cd FROM loja")

        resultados = cursor.fetchall()

        print("\nLoja:")

        for  id_loja, nome_loja,endereco,gerente, id_estoque_cd in resultados:
            print(f"ID: {id_loja} | Nome: {nome_loja}  |  Endereço: {endereco} |  Gerente: {gerente} | ID estoque: {id_estoque_cd}")
        cursor.close()
        conexao.close()