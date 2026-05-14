import mysql.connector
from conexao import conectar

def exibir_dados_loja():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM CADASTRO_LOJA")
        resultados = cursor.fetchall()

        print("\nLoja:")

        for id_loja, nome_loja, cnpj, endereco, telefone, gerente, id_estoque_cd in resultados:
            print(f"ID: {id_loja} | Nome: {nome_loja} | Cnpj: {cnpj} | endereco: { endereco}| Telefone: {telefone}| Gerente: {gerente}| Id estoque: {id_estoque_cd} ")

        cursor.close()
        conexao.close()