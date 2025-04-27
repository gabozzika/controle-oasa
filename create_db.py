import sqlite3

# Criando o banco de dados
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Criando a tabela de usuários
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
''')

# Criando a tabela de requisições
c.execute('''
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        bp TEXT NOT NULL,
        equipment TEXT NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
''')

conn.commit()  # Salva as mudanças no banco de dados
conn.close()   # Fecha a conexão
