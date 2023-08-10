import mysql.connector

conexao = mysql.connector.connect(host= 'localhost', user='root', password='Madrinha3558*', database='bdyoutube')

cursor = conexao.cursor()

#CRUD
#comando = f'' #comando SQL
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados
#resultado = cursor.fetchall() #ler banco de dados

#CREATE
nome_produto = "chocolate"
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})' #comando SQL
cursor.execute(comando)
conexao.commit() #edita o banco de dados


#READ
comando = 'SELECT * FROM vendas' #comando SQL
cursor.execute(comando)
resultado = cursor.fetchall() #ler banco de dados
print(resultado)

#UPDATE
valor = 6
nome_produto = "todynho"
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"' #comando SQL
cursor.execute(comando)
conexao.commit() #edita o banco de dados

#DELETE
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"' #comando SQL
cursor.execute(comando)
conexao.commit() #edita o banco de dados


cursor.close()
conexao.close()