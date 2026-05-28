import mysql.connector
from conexao import conectar

import sys
import os

# adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_loja():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        nome_loja = input("Nome da loja: ")
        cnpj = input("CNPJ: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        gerente = input("Gerente: ")

        sql = """
        select 
            id_estoque_cd, quantidade, local_estoque, prox_pedido
        from estoque_cd
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print ("\nEstoques CD disponíveis: ")
        for dado in resultados:
            print (f"ID: |{dado[0]} |" f"Quantia: {dado[1]} |" f"Local: {dado[2]} |" f"|Próximo pedido: {dado[3]}")
        
        id_estoque_cd = int(input("ID do estoque CD: "))

        sql = "INSERT INTO loja (nome_loja, cnpj, endereco, telefone, gerente, id_estoque_cd) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (nome_loja, cnpj, endereco, telefone, gerente, id_estoque_cd)

        cursor.execute(sql, values)
        conexao.commit()

        print("Loja inserida")

        cursor.close()
        conexao.close()

