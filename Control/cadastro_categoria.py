import mysql.connector
from conexao import conectar

def inserir_dados_categoria():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
    nome_categoria = input ("nome da categoria: ")
    descricao = input ("descrição: ")
    tipo=input ("tipo da categoria: ")
    data_cadastro = input ("data do cadastro: ")
    estampa=input ("estampa: ")
    id_estoque_loja=input ("id do estoque loja: ")
    sql = "INSERT INTO categoria (nome_categoria, descricao, tipo, data_cadastro, estampa, id_estoque_loja) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (nome_categoria, descricao, tipo, data_cadastro, estampa, id_estoque_loja)

    cursor.execute(sql, values)
    conexao.commit()

    print("Categoria inserida")

    cursor.close()
    conexao.close()