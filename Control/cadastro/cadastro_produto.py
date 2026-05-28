import mysql.connector
from conexao import conectar

import sys
import os

# adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def inserir_dados_produto():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        nome=input("Nome do produto: ")
        descricao=input("Descricao: ")
        codigo_barras=input("Codigo de barras: ")
        preco_custo=input("Preço: ")
        unidade_medida=input("Medida: ")

        sql = """
        SELECT
            id_fabricante, nome_fabrica, cidade, tipo_fabrica
        FROM fabricante
        """

        cursor.execute(sql)
        resultados = cursor.fetchall()

        print("\nFabricantes disponíveis:")
        for dado in resultados:
            print(
                f"ID: {dado[0]} |" f"Nome: {dado[1]} |" f"Cidade: {dado[2]} |" f"Tipo: {dado[3]}")

        id_fabricante=input("Id do fabricante: ")

        sql = "INSERT INTO produto (nome,descricao, codigo_barras,preco_custo,unidade_medida,id_fabricante) VALUES (%s, %s, %s,%s,%s,%s)"
        values = (nome,descricao, codigo_barras,preco_custo,unidade_medida,id_fabricante)

        cursor.execute(sql, values)
        conexao.commit()

        print("Produto inserido")

        cursor.close()
        conexao.close()