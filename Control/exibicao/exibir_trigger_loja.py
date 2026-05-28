import mysql.connector
from conexao import conectar

def exibir_logs_loja():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_log_loja, id_loja, acao, endereco_antigo, endereco_novo, usuario, data_alteracao FROM log_loja")
        resultados = cursor.fetchall()

        print("\n===== LOGS DO LOJA =====\n")

        for id_log_loja, id_loja, acao, endereco_antigo, endereco_novo, usuario, data_alteracao in resultados:

            print(f"ID LOG: {id_log_loja} | ID loja: {id_loja} | Ação: {acao} | Endereço antigo: {endereco_antigo} | Endereco novo: {endereco_novo} | Usuário: {usuario} | Data: {data_alteracao}")

        cursor.close()
        conexao.close()