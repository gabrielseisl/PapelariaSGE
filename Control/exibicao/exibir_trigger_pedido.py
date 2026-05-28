import mysql.connector
from conexao import conectar

def exibir_logs_pedido():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_log_pedido, id_pedido, acao, valor_antigo, valor_novo, usuario, data_alteracao FROM log_pedido")
        resultados = cursor.fetchall()

        print("\n===== LOGS DO PEDIDO =====\n")

        for id_log_pedido, id_pedido, acao, valor_antigo, valor_novo, usuario, data_alteracao in resultados:

            print(f"ID LOG: {id_log_pedido} | ID pedido: {id_pedido} | Ação: {acao} | Valor antigo: {valor_antigo} | Valor novo: {valor_novo} | Usuário: {usuario} | Data: {data_alteracao}")

        cursor.close()
        conexao.close()