import mysql.connector
from conexao import conectar

def exibir_dados_loja():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM MOVIMENTACAO")
        resultados = cursor.fetchall()

        print("\nMovimentacao:")

        for id_movimentacao, tipo, quantidade, origem, destino, data_movimentacao, id_categoria in resultados:
            print(f"ID: {id_loja} | Nome: {nome_loja} | Cnpj: {cnpj} | endereco: { endereco}| Telefone: {telefone}| Gerente: {gerente}| Id estoque: {id_estoque_cd} ")

        cursor.close()
        conexao.close()

#terminar