import mysql.connector
from conexao import conectar

import sys
import os

# adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_estoque_cd():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        quantidade = input("Quantidade: ")
        prox_pedido = input("Próximo pedido: ")
        qtd_minima = input("Quantidade mínima: ")
        qtd_maxima = input("Quantidade máxima: ")
        local_estoque = input("Local do estoque: ")
        id_pedido = int(input("ID do pedido: "))

        sql = "INSERT INTO estoque_cd (quantidade, prox_pedido, qtd_minima, qtd_maxima, local_estoque, id_pedido) VALUES (%s, %s, %s, %s, %s, %s)"

        values = (quantidade, prox_pedido, qtd_minima, qtd_maxima, local_estoque, id_pedido)

        cursor.execute(sql, values)
        conexao.commit()

        print("Estoque CD inserido")

        cursor.close()
        conexao.close()

