import mysql.connector
from conexao import conectar

import sys
import os

# adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar


def inserir_dados_pedido():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        data_pedido = input("Data Pedido: ")
        data_entrega = input("Data Entrega: ")
        valor_total = float(input("Valor: "))
        quantia_itens = int(input("Quantidade: "))
        entrega_status = input("Status: ")
        id_fornecedor = int(input("Id do fornecedor: "))

        sql = "INSERT INTO pedido (data_pedido, data_entrega, valor_total, quantia_itens, entrega_status, id_fornecedor) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (data_pedido, data_entrega, valor_total, quantia_itens, entrega_status, id_fornecedor)

        cursor.execute(sql, values)
        conexao.commit()

        print("Pedido inserido")

        cursor.close()
        conexao.close()