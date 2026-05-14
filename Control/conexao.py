import mysql.connector

def conectar():
    
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="papelaria_sg"
    )
    print("conectado")
    return conexao
