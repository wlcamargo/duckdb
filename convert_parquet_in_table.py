import duckdb

# Nome do arquivo do banco de dados DuckDB
db_file = "database.db"

# Supondo que o arquivo Parquet está localizado em "C:/Users/walla/OneDrive - Educacional/Ambiente de Trabalho/source_parquet/estabelecimentos.parquet"
parquet_file = "C:/Users/walla/OneDrive - Educacional/Ambiente de Trabalho/source_parquet/estabelecimentos.parquet"

# Estabelece conexão com o DuckDB
conn = duckdb.connect(database=db_file, read_only=False)

# Cria uma tabela no DuckDB e carrega os dados do arquivo Parquet nela
conn.execute(f"CREATE TABLE estabelecimentos AS SELECT * FROM parquet_scan('{parquet_file}")

# Fecha a conexão com o DuckDB
conn.close()
