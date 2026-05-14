import mysql.connector
from conexao import conectar

def exibir_dados_estoque_cd():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM ESTOQUE_CD")
        resultados = cursor.fetchall()

        print("\nEstoque_cd:")

        for id_estoque_cd, quantidade, prox_pedido, qtd_minima, qtd_maxima, local_estoque, id_pedido in resultados:
            print(f"ID: {id_estoque_cd} | Quantidade: {quantidade} | Próximo pedido: {prox_pedido}| Quantia mínima: {qtd_minima}| Quantia máxima: {qtd_maxima}| Local do estoque: {local_estoque}| Id pedido: {id_pedido} ")

        cursor.close()
        conexao.close()