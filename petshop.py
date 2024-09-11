import sqlite3
conn = sqlite3.connect('petshop.db')
cursor = conn.cursor()
# Criar a tabela Clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clientes (
   id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
   nome TEXT NOT NULL,
   telefone TEXT NOT NULL,
   email TEXT
)
''')
# Criar a tabela Pets
cursor.execute('''
CREATE TABLE IF NOT EXISTS Pets (
   id_pet INTEGER PRIMARY KEY AUTOINCREMENT,
   nome TEXT NOT NULL,
   tipo TEXT NOT NULL,
   raca TEXT NOT NULL,
   id_dono INTEGER NOT NULL,
   FOREIGN KEY (id_dono) REFERENCES Clientes (id_cliente)
)
''')
# Criar a tabela Agendamentos
cursor.execute('''
CREATE TABLE IF NOT EXISTS Agendamentos (
   id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
   id_cliente INTEGER NOT NULL,
   id_pet INTEGER NOT NULL,
   data_agendamento TEXT NOT NULL,
   hora_agendamento TEXT NOT NULL,
   servico TEXT NOT NULL,
   FOREIGN KEY (id_cliente) REFERENCES Clientes (id_cliente),
   FOREIGN KEY (id_pet) REFERENCES Pets (id_pet)
)
''')
# Inserir novo cliente
cursor.execute('''
INSERT INTO Clientes (nome, telefone, email) 
VALUES (?, ?, ?)
''', ('John Doe', '123-456-7890', 'john.doe@example.com'))

# Confirmar as alterações e fechar a conexão
conn.commit()
conn.close()
print("Banco de dados e tabelas criados com sucesso.")
