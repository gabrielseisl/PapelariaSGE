import mysql.connector
from conexao import conectar

import sys
import os

# adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_movimentacao():

    conexao = conectar()


    if conexao:
        cursor = conexao.cursor()

        tipo = input("Tipo de movimentação: ")
        quantidade = input("Quantidade: ")
        origem = input("Origem: ")
        destino = input("Destino: ")
        data_movimentacao = input("Data da movimentação: ")
        id_categoria = int(input("ID da categoria: "))

        sql = "INSERT INTO movimentacao (tipo, quantidade, origem, destino, data_movimentacao, id_categoria) VALUES (%s, %s, %s, %s, %s, %s)"

        values = (tipo, quantidade, origem, destino, data_movimentacao, id_categoria)

        cursor.execute(sql, values)
        conexao.commit()

        print("Movimentação inserida")

        cursor.close()
        conexao.close()

