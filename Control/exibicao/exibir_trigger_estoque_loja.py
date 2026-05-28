import mysql.connector
from conexao import conectar

def exibir_logs_estoque_loja():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_log_estoque_loja, id_estoque_loja, acao, valor_antigo, valor_novo, usuario, data_alteracao FROM log_estoque_loja")
        resultados = cursor.fetchall()

        print("\n===== LOGS DO ESTOQUE LOJA =====\n")

        for id_log_estoque_loja, id_estoque_loja, acao, valor_antigo, valor_novo, usuario, data_alteracao in resultados:

            print(f"ID LOG: {id_log_estoque_loja} | ID Estoque: {id_estoque_loja} | Ação: {acao} | Valor antigo: {valor_antigo} | Valor novo: {valor_novo} | Usuário: {usuario} | Data: {data_alteracao}")

        cursor.close()
        conexao.close()