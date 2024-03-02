import duckdb

# Nome do arquivo do banco de dados DuckDB
db_file = "database.db"

# Estabelece conexão com o DuckDB
conn = duckdb.connect(database=db_file, read_only=True)

# Executa uma consulta para obter o nome de todas as tabelas no banco de dados
result = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Recupera todas as linhas do resultado da consulta
tables = result.fetchall()

# Exibe os nomes das tabelas
for table in tables:
    print(table[0])

# Fecha a conexão com o DuckDB
conn.close()

