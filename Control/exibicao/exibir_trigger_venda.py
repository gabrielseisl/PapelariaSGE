import mysql.connector
from conexao import conectar

def exibir_logs_venda():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_log_venda, id_venda, acao, lucro_antigo, lucro_novo, usuario, data_alteracao FROM log_venda")
        resultados = cursor.fetchall()

        print("\n===== LOGS DE VENDA =====\n")

        for id_log_venda, id_venda, acao, lucro_antigo, lucro_novo, usuario, data_alteracao in resultados:

            print(f"ID LOG: {id_log_venda} | ID venda: {id_venda} | Ação: {acao} | Lucro antigo: {lucro_antigo} | Lucro novo: {lucro_novo} | Usuário: {usuario} | Data: {data_alteracao}")

        cursor.close()
        conexao.close()