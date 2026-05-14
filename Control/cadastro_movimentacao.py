import mysql.connector
from conexao import conectar

def inserir_dados_movimentacao():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
    tipo=input ("tipo de movimentação: ")
    quantidade = input ("quantidade: ")
    origem=input ("origem: ")
    destino=input ("destino: ")
    data_movimentacao=input ("data da movimentação: ")
    id_categoria=input ("id da categoria: ")
    sql = "INSERT INTO movimentacao (tipo,quantidade,origem,destino,data_movimentacao,id_categoria) VALUES (%s, %s, %s,%s,%s,%s)"
    values = (tipo,quantidade,origem,destino,data_movimentacao,id_categoria)

    cursor.execute(sql, values)
    conexao.commit()

    print("Movimentação inserida")

    cursor.close()
    conexao.close()