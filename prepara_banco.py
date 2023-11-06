import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `PORTAL`;")

cursor.execute("CREATE DATABASE `PORTAL`;")

cursor.execute("USE `PORTAL`;")

# criando tabelas
TABLES = {}

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `nickname` varchar(50) NOT NULL,
      `senha` varchar(100) NOT NULL,
      `departamento` varchar(20) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nickname, senha, departamento) VALUES (%s, %s, %s)'
usuarios = [
      ("Administrador", generate_password_hash("produm@r").decode("utf-8"), "TI"),
      ("SILAS", generate_password_hash("12345").decode("utf-8"), "TI"),
      ("WALDENOR", generate_password_hash("1722@").decode("utf-8"), "TI")
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from PORTAL.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()