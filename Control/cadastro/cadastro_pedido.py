import mysql.connector
from conexao import conectar

import sys
import os

# adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

from datetime import datetime

def inserir_dados_pedido():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        data_pedido = input("Data Pedido: ")
        data_pedido = datetime.strptime(data_pedido,"%d/%m/%Y").strftime("%Y-%m-%d")
        data_entrega = input("Data Entrega: ")
        data_entrega = datetime.strptime(data_entrega,"%d/%m/%Y").strftime("%Y-%m-%d")
        valor_total = float(input("Valor: "))
        quantia_itens = int(input("Quantidade: "))
        entrega_status = input("Status: ")

        sql = """
        select 
            id_fornecedor, nome_fornecedor, prazo_entrega
        from fornecedor 
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print ("\nFornecedores disponíveis: ")
        for dado in resultados:
            print (f"ID: {dado[0]} |" f"Fornecedor: {dado[1]} |" f"Prazo de entrega: {dado[2]}")
            
        id_fornecedor = int(input("Id do fornecedor: "))

        sql = "INSERT INTO pedido (data_pedido, data_entrega, valor_total, quantia_itens, entrega_status, id_fornecedor) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (data_pedido, data_entrega, valor_total, quantia_itens, entrega_status, id_fornecedor)

        cursor.execute(sql, values)
        conexao.commit()

        print("Pedido inserido")

        cursor.close()
        conexao.close()