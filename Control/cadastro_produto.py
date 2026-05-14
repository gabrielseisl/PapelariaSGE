import mysql.connector
from conexao import conectar

def inserir_dados_produto():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        nome=input("Nome do produto: ")
        descricao=input("Descricao: ")
        codigo_barras=input("Codigo de barras: ")
        preco_custo=input("Preço: ")
        unidade_medida=input("Medida: ")
        id_fabricante=input("Id do fabricante: ")

        sql = "INSERT INTO produto (nome,descricao, codigo_barras,preco_custo,unidade_medida,id_fabricante) VALUES (%s, %s, %s,%s,%s,%s)"
        values = (nome,descricao, codigo_barras,preco_custo,unidade_medida,id_fabricante)

        cursor.execute(sql, values)
        conexao.commit()

        print("Produto inserido")

        cursor.close()
        conexao.close()
