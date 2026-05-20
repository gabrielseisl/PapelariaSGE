import mysql.connector
from conexao import conectar

def exibir_logs_estoque():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_log, id_estoque_cd, acao, valor_antigo, valor_novo, usuario, data_alteracao FROM log_estoque_cd")
        resultados = cursor.fetchall()

        print("\n===== LOGS DO ESTOQUE =====\n")

        for id_log, id_estoque_cd, acao, valor_antigo, valor_novo, usuario, data_alteracao in resultados:

            print(f"ID LOG: {id_log} | ID Estoque: {id_estoque_cd} | Ação: {acao} | Valor antigo: {valor_antigo} | Valor novo: {valor_novo} | Usuário: {usuario} | Data: {data_alteracao}")

        cursor.close()
        conexao.close()
   