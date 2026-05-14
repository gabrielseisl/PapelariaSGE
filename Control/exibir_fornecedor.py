import mysql.connector
from conexao import conectar

def exibir_dados_fornecedor():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM FORNECEDOR")
        resultados = cursor.fetchall()

        print("\nFornecedor:")

        for id_fornecedor, nome_fornecedor, cnpj, telefone, email, prazo_entrega, id_produto in resultados:
            print(f"ID: {id_fornecedor} | Nome: {nome_fornecedor} | CNPJ: {cnpj}| Telefone: {telefone}| Email: {email}| Prazo: {prazo_entrega}| Id produto: {id_produto} ")

        cursor.close()
        conexao.close()