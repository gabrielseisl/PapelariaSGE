import mysql.connector
from conexao import conectar


def exibir_dados_pedido():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_pedido, data_pedido, data_entrega, valor_total, quantia_itens, entrega_status, id_fornecedor FROM pedido")
        resultados = cursor.fetchall()

        print("\nPedido:")

        for id_pedido, data_pedido, data_entrega, valor_total, quantia_itens, entrega_status, id_fornecedor in resultados:
            print(f"ID: {id_pedido} | Data pedido: {data_pedido} | Data entrega: {data_entrega} | Valor total: {valor_total} | Quantia itens: {quantia_itens} | Status entrega: {entrega_status} | ID fornecedor: {id_fornecedor}")

        cursor.close()
        conexao.close()
