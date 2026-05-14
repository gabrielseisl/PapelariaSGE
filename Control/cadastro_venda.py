import mysql.connector
from conexao import conectar

def inserir_dados_vendas():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
    quantidade=input("Quantidade: ")
    preco_venda=input("Preço: ")
    lucro=input("Lucro: ")
    forma_pagamento=input("Forma de pagamento: ")
    data_venda=input("Data da venda: ")
    id_movimentacao=input("Id da movimentação: ")

    sql = "INSERT INTO venda (quantidade,preco_venda,lucro,forma_pagamento,data_venda,id_movimentacao) VALUES (%s, %s, %s,%s,%s,%s)"
    values = (quantidade,preco_venda,lucro,forma_pagamento,data_venda,id_movimentacao)

    cursor.execute(sql, values)
    conexao.commit()

    print("Venda inserida")

    cursor.close()
    conexao.close()