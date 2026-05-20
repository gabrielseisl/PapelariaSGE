import mysql.connector
from conexao import conectar

def exibir_dados_estoque_loja():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_estoque_loja, quantidade, prox_pedido, qtd_minima, qtd_maxima,id_loja from estoque_loja")
        resultados = cursor.fetchall()

        print("\nEstoque_loja:")

        for id_estoque_loja, quantidade, prox_pedido, qtd_minima, qtd_maxima, id_loja in resultados:
            print(f"ID: {id_estoque_loja} | Quantidade: {quantidade} | Próximo pedido: {prox_pedido}| Quantia mínima: {qtd_minima}| Quantia máxima: {qtd_maxima}| Id loja: {id_loja} ")

        cursor.close()
        conexao.close()