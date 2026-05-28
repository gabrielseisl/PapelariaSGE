import mysql.connector
import sys
import os
import sessaobadass

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_log_movimentacao():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_movimentacao = input("ID da movimentação: ")
        acao = input("Ação: ")
        valor_antigo = input("Valor antigo: ")
        valor_novo = input("Valor novo: ")
        usuario = sessaobadass.usuario_mudou()


        sql = "INSERT INTO log_movimentacao (id_movimentacao, acao, valor_antigo, valor_novo, usuario) VALUES (%s, %s, %s, %s, %s)"

        values = (id_movimentacao, acao, valor_antigo, valor_novo, usuario)

        cursor.execute(sql, values)
        conexao.commit()

        print("Mudança feita com sucesso!")

        cursor.close()
        conexao.close()