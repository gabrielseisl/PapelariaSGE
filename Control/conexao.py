import mysql.connector

def conectar():
    
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="papelaria_sg"
    )
    print("você foi conectado com sucesso ao sistema da papelaria sge")
    return conexao
