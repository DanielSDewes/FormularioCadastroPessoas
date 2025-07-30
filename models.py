import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""
DROP TABLE IF EXISTS pessoas
""")

c.execute("""
-- Criação da tabela pessoas
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cep TEXT,
    rua TEXT,
    cidade TEXT,
    estado TEXT,
    cpf TEXT NOT NULL UNIQUE
)
""")

conn.commit()
conn.close()
