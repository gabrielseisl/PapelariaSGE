import mysql.connector
from conexao import conectar

def inserir_dados_fornecedor():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        nome_fornecedor=input("Nome do fornecedor: ")
        cnpj=input("Cnpj: ")
        telefone=input("Telefone: ")
        email=input("Email: ")
        prazo_entrega=input("Prazo da entrega: ")
        id_produto=input("Id do produto: ")
        sql = "INSERT INTO fornecedor (nome_fornecedor,cnpj,telefone,email,prazo_entrega,id_produto) VALUES (%s, %s, %s,%s,%s,%s)"
        values = (nome_fornecedor,cnpj,telefone,email,prazo_entrega,id_produto)

        cursor.execute(sql, values)
        conexao.commit()

        print("Fornecedor inserido")

        cursor.close()
        conexao.close()
