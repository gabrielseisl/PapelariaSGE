import mysql.connector
from conexao import conectar

import sys
import os

# adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

from datetime import datetime

def inserir_dados_estoque_cd():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        quantidade = input("Quantidade: ")
        prox_pedido = input("Próximo pedido: ")
        prox_pedido = datetime.strptime(prox_pedido,"%d/%m/%Y").strftime("%Y-%m-%d")
        qtd_minima = input("Quantidade mínima: ")
        qtd_maxima = input("Quantidade máxima: ")
        local_estoque = input("Local do estoque: ")

        sql = """
        select 
            id_pedido, data_pedido, valor_total, entrega_status
        from pedido
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print ("\nPedidos disponíveis: ")
        for dado in resultados:
            print (f"Id: {dado[0]} |" f"Data pedido: {dado[1]} |" f"Valor: {dado[2]} |" f"Status: {dado[3]}")
        
        id_pedido = int(input("ID do pedido: "))

        sql = "INSERT INTO estoque_cd (quantidade, prox_pedido, qtd_minima, qtd_maxima, local_estoque, id_pedido) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (quantidade, prox_pedido, qtd_minima, qtd_maxima, local_estoque, id_pedido)

        cursor.execute(sql, values)
        conexao.commit()

        print("Estoque CD inserido")

        cursor.close()
        conexao.close()