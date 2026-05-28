import mysql.connector
from conexao import conectar

import sys
import os

# adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

from datetime import datetime

def inserir_dados_movimentacao():

    conexao = conectar()


    if conexao:
        cursor = conexao.cursor()

        tipo = input("Tipo de movimentação: ")
        quantidade = input("Quantidade: ")
        origem = input("Origem: ")
        destino = input("Destino: ")
        data_movimentacao = input("Data da movimentação: ")
        data_movimentacao = datetime.strptime(data_movimentacao,"%d/%m/%Y").strftime("%Y-%m-%d")

        sql = """
        select 
            id_categoria, nome_categoria, tipo
        from categoria
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print("\nCategorias disponíveis: ")
        for dado in resultados:
            print (f"ID: {dado[0]} |" f"Categoria: {dado[1]} |" f"Tipo: {dado[2]}")

        id_categoria = int(input("ID da categoria: "))

        sql = "INSERT INTO movimentacao (tipo, quantidade, origem, destino, data_movimentacao, id_categoria) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (tipo, quantidade, origem, destino, data_movimentacao, id_categoria)

        cursor.execute(sql, values)
        conexao.commit()

        print("Movimentação inserida")

        cursor.close()
        conexao.close()

