import mysql.connector
import sys
import os
import sessaobadass

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_log_venda():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_venda = input("ID do produto: ")
        acao = input("Ação: ")
        lucro_antigo = input("Lucro antigo: ")
        lucro_novo = input("Lucro novo: ")
        usuario = sessaobadass.usuario_mudou()
    
        sql = "INSERT INTO  log_venda(id_venda, acao, lucro_antigo, lucro_novo, usuario) VALUES (%s, %s, %s, %s, %s)"

        values = (id_venda, acao, lucro_antigo, lucro_novo, usuario)

        cursor.execute(sql, values)
        conexao.commit()

        print("Mudança feita com sucesso!")

        cursor.close()
        conexao.close()