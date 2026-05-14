import mysql.connector
from conexao import conectar

def exibir_dados_estoque_categoria():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM categoria")
        resultados = cursor.fetchall()

        print("\nCategoria:")

        for id_categoria, nome_categoria,descricao,tipo,data_cadas in resultados:
            print(f"ID: {id_categoria} | Nome: {nome} | Descrição: {descricao} ")

        cursor.close()
        conexao.close()