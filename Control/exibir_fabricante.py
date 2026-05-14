import mysql.connector
from conexao import conectar

def exibir_dados_fabricante():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM FABRICANTE")
        resultados = cursor.fetchall()

        print("\nFabricantes:")

        for id_fabricante, nome_fabrica, cnpj,telefone,email,cidade,tipo_fabrica in resultados:
            print(f"ID: {id_fabricante} | Nome: {nome_fabrica} | Cnpj: {cnpj}| Telefone: {telefone}| Email: {email}| Cidade: {cidade}|Tipo: {tipo_fabrica} ")

        cursor.close()
        conexao.close()
