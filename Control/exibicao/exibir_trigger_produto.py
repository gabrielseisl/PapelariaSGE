import mysql.connector
from conexao import conectar

def exibir_logs_produto():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_log_produto, id_produto, acao, valor_antigo, valor_novo, usuario, data_alteracao FROM log_produto")
        resultados = cursor.fetchall()

        print("\n===== LOGS DO PRODUTO =====\n")

        for id_log_produto, id_produto, acao, valor_antigo, valor_novo, usuario, data_alteracao in resultados:

            print(f"ID LOG: {id_log_produto} | ID produto: {id_produto} | Ação: {acao} | Valor antigo: {valor_antigo} | Valor novo: {valor_novo} | Usuário: {usuario} | Data: {data_alteracao}")

        cursor.close()
        conexao.close()