import mysql.connector
from conexao import conectar

def exibir_dados_fornecedor():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_fornecedor, nome_fornecedor, prazo_entrega, id_produto FROM fornecedor")
        resultados = cursor.fetchall()

        print("\nFornecedor:")

        for id_fornecedor, nome_fornecedor,prazo_entrega, id_produto in resultados:
            print(f"ID: {id_fornecedor} | Nome: {nome_fornecedor} | Prazo: {prazo_entrega} | ID produto: {id_produto}")
        cursor.close()
        conexao.close()