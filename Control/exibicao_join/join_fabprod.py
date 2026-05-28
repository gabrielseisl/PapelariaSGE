import mysql.connector
from conexao import conectar

def exibir_join_fabprod():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("select f.nome_fabrica,f.tipo_fabrica as fabricante,p.nome,p.preco_custo from produto p inner join fabricante f on p.id_fabricante=f.id_fabricante")
        resultados = cursor.fetchall()

        print("\n Fabricante/Produto:")

       
    for nome_fabrica, tipo_fabrica, nome, preco_custo in resultados:

        print(f"Nome fabrica: {nome_fabrica} | Tipo fabrica: {tipo_fabrica} | Nome produto: {nome} | Preço de custo:{ preco_custo}")

        cursor.close()
        conexao.close()