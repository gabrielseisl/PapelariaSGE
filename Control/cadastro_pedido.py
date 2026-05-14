import mysql.connector
from conexao import conectar

def inserir_dados_pedido():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        data_pedido = input ("data do pedido:"),
        data_entrega = input ("data entrega:"),
        valor_total = input ("valor total:"),
        quantia_itens = input ("quantia de itens:"),
        entrega_status = input ("status da entrega"),
        id_fornecedor = input ("id do fornecedor"),
        sql = "INSERT INTO pedido (data_pedido, data_entrega,valor_total,quantia_itens,entrega_status,id_fornecedor) VALUES (%s, %s, %s,%s,%s,%s)"
        values = (data_pedido, data_entrega,valor_total,quantia_itens,entrega_status,id_fornecedor)

        cursor.execute(sql, values)
        conexao.commit()

        print("Pedido inserido")

        cursor.close()
        conexao.close()