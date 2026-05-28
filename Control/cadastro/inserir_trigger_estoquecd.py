import mysql.connector
import sys
import os
import sessaobadass
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_log_estoque_cd():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_estoque_cd = input("ID do estoque CD: ")
        acao = input("Ação: ")
        valor_antigo = input("Valor antigo: ")
        valor_novo = input("Valor novo: ")
        usuario = sessaobadass.usuario_mudou()

        sql = "INSERT INTO log_estoque_cd (id_estoque_cd, acao, valor_antigo, valor_novo, usuario) VALUES (%s, %s, %s, %s, %s)"

        values = (id_estoque_cd, acao, valor_antigo, valor_novo, usuario)

        cursor.execute(sql, values)
        conexao.commit()

        print("Mudança feita com sucesso!")

        cursor.close()
        conexao.close()