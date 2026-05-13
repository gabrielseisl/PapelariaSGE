import mysql.connector
from conexao import conectar

def inserir_dados():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        nome_fabrica=input("nome: ")
        cnpj=input("cnpj: ")
        telefone=input("telefone: ")
        email=input("email: ")
        cidade=input("cidade: ")
        tipo_fabrica =input("tipo da fabrica: ")

        sql = "INSERT INTO fabricante (nome_fabrica,cnpj,telefone,email,cidade,tipo_fabrica) VALUES (%s, %s, %s,%s,%s,%s)"
        values = (nome_fabrica,cnpj,telefone,email,cidade,tipo_fabrica)

        cursor.execute(sql, values)
        conexao.commit()

        print("Fabricante inserido")

        cursor.close()
        conexao.close()
