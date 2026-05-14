import mysql.connector
from conexao import conectar

def inserir_dados_estoque_loja():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
quantidade=input("Quantidade: ")
prox_pedido=input("Data pedido: ")
qtd_minima=input("Quantidade minima: ")
qtd_maxima=input("Quantidade maxima: ")
preco_estoque=input("Preço: ")
id_loja=input("Id da loja: ")
sql = "INSERT INTO estoque_loja (quantidade,prox_pedido,qtd_minima,qtd_maxima,preco_estoque,id_loja) VALUES (%s, %s, %s,%s,%s,%s)"
values = (quantidade,prox_pedido,qtd_minima,qtd_maxima,preco_estoque,id_loja)

cursor.execute(sql, values)
conexao.commit()

print("Estoque loja inserido")

cursor.close()
conexao.close()