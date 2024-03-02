import duckdb

# Nome do arquivo do banco de dados DuckDB
db_file = "database.db"

# Estabelece conexão com o DuckDB
conn = duckdb.connect(database=db_file, read_only=True)

# Executa uma consulta para selecionar as 10 primeiras linhas da tabela
result = conn.execute(""" SELECT * FROM estabelecimentos limit(10) """)

# Recupera todas as linhas do resultado da consulta
rows = result.fetchall()

# Exibe as linhas recuperadas
for row in rows:
    print(row)

# Fecha a conexão com o DuckDB
conn.close()
