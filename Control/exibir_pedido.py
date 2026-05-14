import mysql.connector
from conexao import conectar

def exibir_dados_pedido():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM PEDIDO")
        resultados = cursor.fetchall()

        print("\nPedido:")

        for id_pedido, data_pedido, data_entrega, valor_total, quantia_itens, unidade_medida, id_fabricante in resultados:
            print(f"ID: {id_pedido} | Data de pedido: {data_pedido} | Data de entrega: {data_entrega}| Valor total: {valor_total}| Quantia itens: {quantia_itens}| Custo: {preco_custo}| Unidade e medida: {unidade_medida}| Id fabricante: {id_fabricante} ")

        cursor.close()
        conexao.close()

        #terminar de trocar os dados