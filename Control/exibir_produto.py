import mysql.connector
from conexao import conectar

def exibir_dados_produto():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM PRODUTO")
        resultados = cursor.fetchall()

        print("\nProduto:")

        for id_produto, nome, descricao, codigo_barras, preco_custo, unidade_medida, id_fabricante in resultados:
            print(f"ID: {id_produto} | Nome: {nome} | Descrição: {descricao}| Codigo de barras: {codigo_barras}| Custo: {preco_custo}| Unidade e medida: {unidade_medida}| Id fabricante: {id_fabricante} ")

        cursor.close()
        conexao.close()