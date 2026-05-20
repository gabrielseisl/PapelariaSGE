import mysql.connector
from conexao import conectar

def exibir_dados_estoque_categoria():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_categoria, nome_categoria, descricao, tipo, data_cadastro, estampa, id_estoque_loja FROM categoria")
        resultados = cursor.fetchall()

        print("\nCategoria:")

        for id_categoria, nome_categoria, descricao, tipo, data_cadastro, estampa, id_estoque_loja in resultados:
            print(f"ID: {id_categoria} | Nome: {nome_categoria} | Descrição: {descricao} | Tipo: {tipo} | Data Cadastro: {data_cadastro} | Estampa: {estampa} | ID Estoque Loja: {id_estoque_loja}")
            
        cursor.close()
        conexao.close()