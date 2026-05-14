import mysql.connector
from conexao import conectar

def inserir_dados_estoque_cd():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
    quantidade=input("Quantidade: ")
    prox_pedido=input("Proximo pedido: ")
    qtd_minima=input("Quantidade minima: ")
    qtd_maxima=input("Quantidade maxima: ")
    local_estoque=input("Local do estoque: ")
    id_pedido=input("Id do pedido: ")
    sql = "INSERT INTO estoque_cd (nome_fornecedor,cnpj,telefone,email,prazo_entrega,id_produto) VALUES (%s, %s, %s,%s,%s,%s)"
    values = (quantidade,prox_pedido,qtd_minima,qtd_maxima,local_estoque,id_pedido)

    cursor.execute(sql, values)
    conexao.commit()

    print("Estoque inserido")

    cursor.close()
    conexao.close()