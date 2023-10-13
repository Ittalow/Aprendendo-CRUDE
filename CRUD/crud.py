import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="4721",
    database="bdyoutube",
)

cursor = conexao.cursor()

# CRUD

# CREATE
nome_produto = "balinha"
valor = 2
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()

# READ
comando = f"SELECT * FROM vendas"
cursor.execute(comando)
resultado = cursor.fetchall()  # ESSE COMANDO LER O BANCO DE DADOS
print(resultado)

# UPDATE
nome_produto = "Sucrilhos"
valor = 4
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

# DELETE
nome_produto = "Sucrilhos"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()
