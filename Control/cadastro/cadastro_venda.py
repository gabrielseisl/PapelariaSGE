import mysql.connector
from conexao import conectar

import sys
import os

# adiciona a pasta raiz do projeto ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

from datetime import datetime

def inserir_dados_vendas():

    conexao = conectar()


    if conexao:
        cursor = conexao.cursor()

        quantidade = input("Quantidade: ")
        preco_venda = input("Preço: ")
        lucro = input("Lucro: ")
        forma_pagamento = input("Forma de pagamento: ")
        data_venda = input("Data da venda: ")
        data_venda = datetime.strptime(data_venda,"%d/%m/%Y").strftime("%Y-%m-%d")

        sql = """
        select 
            id_movimentacao, tipo, origem, destino
        from movimentacao
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print("\nMovimentações disponíveis: ")
        for dado in resultados:
            print (f"ID: {dado[0]} |" f"Tipo: {dado[1]} |" f"Origem: {dado[2]} |" f"Destino: {dado[3]}")
        
        id_movimentacao = int(input("ID da movimentação: "))

        sql = "INSERT INTO venda (quantidade, preco_venda, lucro, forma_pagamento, data_venda, id_movimentacao) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (quantidade, preco_venda, lucro, forma_pagamento, data_venda, id_movimentacao)

        cursor.execute(sql, values)
        conexao.commit()

        print("Venda inserida")

        cursor.close()
        conexao.close()
