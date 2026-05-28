import mysql.connector
from conexao import conectar

import sys
import os

# adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

from datetime import datetime

def inserir_dados_fornecedor():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        nome_fornecedor=input("Nome do fornecedor: ")
        cnpj=input("Cnpj: ")
        telefone=input("Telefone: ")
        email=input("Email: ")
        prazo_entrega=input("Prazo da entrega: ")
        prazo_entrega = datetime.strptime(prazo_entrega,"%d/%m/%Y").strftime("%Y-%m-%d")

        sql = """
        SELECT
            id_produto, nome, descricao, preco_custo
        FROM produto
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print("\nProdutos disponíveis:")
        for dado in resultados:
            print(f"ID: {dado[0]} |" f"Produto: {dado[1]} |" f"Descrição: {dado[2]} |" f"Preço: {dado[3]}")

        id_produto=input("Id do produto: ")

        sql = "INSERT INTO fornecedor (nome_fornecedor,cnpj,telefone,email,prazo_entrega,id_produto) VALUES (%s, %s, %s,%s,%s,%s)"
        values = (nome_fornecedor,cnpj,telefone,email,prazo_entrega,id_produto)

        cursor.execute(sql, values)
        conexao.commit()

        print("Fornecedor inserido")

        cursor.close()
        conexao.close()
