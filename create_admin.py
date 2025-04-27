import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Inserir o usuário admin manualmente (com o username 'admin' e uma senha de sua escolha)
username = 'admin'
password = '1234'  # Substitua 'senha_admin' pela senha que você deseja
role = 'admin'

# Inserindo o admin na tabela users
c.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))

conn.commit()  # Salva as mudanças no banco de dados
conn.close()   # Fecha a conexão

print("Usuário admin criado com sucesso!")
