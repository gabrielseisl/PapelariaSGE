import mysql.connector
from conexao import conectar

def exibir_join_movivenda():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("select m.origem,v.quantidade,v.forma_pagamento from movimentacao m left join venda v on m.id_movimentacao=v.id_movimentacao")
        resultados = cursor.fetchall()

        print("\n Movimentação/Venda:")

       
    for origem,quantidade,forma_pagamento in resultados:

        print(f"Origem: {origem} | Quantidade: {quantidade} | Forma de pagamento: {forma_pagamento} ")

        cursor.close()
        conexao.close()