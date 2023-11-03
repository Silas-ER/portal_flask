SECRET_KEY = 'produmar' #criptografar

#configuracoes de banco de dados
SQLALCHEMY_DATABASE_URI = \
    '{SGBB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBB = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'PORTAL',
    )

