import mysql.connector
from conexao import conectar

import sys
import os

# adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

from datetime import datetime

def inserir_dados_estoque_loja():

    conexao = conectar()


    if conexao:
        cursor = conexao.cursor()

        quantidade = input("Quantidade: ")
        prox_pedido = input("Data pedido: ")
        prox_pedido = datetime.strptime(prox_pedido,"%d/%m/%Y").strftime("%Y-%m-%d")
        qtd_minima = input("Quantidade minima: ")
        qtd_maxima = input("Quantidade maxima: ")
        preco_estoque = input("Preço: ")

        sql = """
        select 
            id_loja, nome_loja, gerente
        from loja
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print ("\nLojas disponíveis: ")
        for dado in resultados:
            print (f"ID: {dado[0]} |" f"Loja: {dado[1]} |" f"Gerente: {dado[2]}")
            
        id_loja = input("Id da loja: ")

        sql = "INSERT INTO estoque_loja (quantidade, prox_pedido, qtd_minima, qtd_maxima, preco_estoque, id_loja) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (quantidade, prox_pedido, qtd_minima, qtd_maxima, preco_estoque, id_loja)

        cursor.execute(sql, values)
        conexao.commit()

        print("Estoque loja inserido")

        cursor.close()
        conexao.close()
