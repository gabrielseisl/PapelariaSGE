import mysql.connector
from conexao import conectar

def inserir_dados_loja():

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
    nome_loja=input("Nome da loja: ")
    cnpj=input("CNPJ: ")
    endereco=input("Endereço: ")
    telefone=input("Telefone: ")
    gerente=input("Gerente: ")
    id_estoque_cd=input("Id do estoque CD: ")

    sql = "INSERT INTO loja (nome_loja,cnpj,endereco,telefone,gerente,id_estoque_cd) VALUES (%s, %s, %s,%s,%s,%s)"
    values = (nome_loja,cnpj,endereco,telefone,gerente,id_estoque_cd)

    cursor.execute(sql, values)
    conexao.commit()

    print("Loja inserida")

    cursor.close()
    conexao.close()