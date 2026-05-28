import mysql.connector
from conexao import conectar

def exibir_join_estoloja():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("select e.quantidade,l.nome_loja,l.endereco from estoque_loja e left join loja l on l.id_loja = e.id_loja")
        resultados = cursor.fetchall()

        print("\n Estoque Loja/Loja:")

       
    for quantidade,nome_loja,endereco in resultados:

        print(f"Quantidade: {quantidade} | Nome Loja {nome_loja} |  Endereço: {endereco}")

        cursor.close()
        conexao.close()