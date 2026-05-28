import mysql.connector
import sys
import os
import sessaobadass

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_log_pedido():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        id_pedido = input("ID do pedido: ")
        acao = input("Ação: ")
        valor_antigo = input("Valor antigo: ")
        valor_novo = input("Valor novo: ")
        usuario = sessaobadass.usuario_mudou()
    
        sql = "INSERT INTO log_pedido (id_pedido, acao, valor_antigo, valor_novo, usuario) VALUES (%s, %s, %s, %s, %s)"

        values = (id_pedido, acao, valor_antigo, valor_novo, usuario)

        cursor.execute(sql, values)
        conexao.commit()

        print("Mudança feita com sucesso!")

        cursor.close()
        conexao.close()