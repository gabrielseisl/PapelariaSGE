import mysql.connector
from conexao import conectar

def exibir_join_fornedido():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("select f.nome_fornecedor,f.prazo_entrega as fornecedor,p.valor_total,p.entrega_status from pedido p inner join fornecedor f on p.id_fornecedor=f.id_fornecedor")
        resultados = cursor.fetchall()

        print("\n Fornecimento/Pedido:")

       
    for nome_fornecedor,prazo_entrega,valor_total,entrega_status in resultados:

        print(f"Nome fornecedor: {nome_fornecedor} | Prazo entrega: {prazo_entrega} | Valor total: {valor_total} | Entrega status:{entrega_status}")

        cursor.close()
        conexao.close()