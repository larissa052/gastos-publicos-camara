import psycopg2

# Configuração da conexão
DB_CONFIG = {
    "dbname": "GASTOS_CAMARA",  # Nome do banco de dados
    "user": "postgres",         # Usuário
    "password": "senha",    # Senha do usuário
    "host": "localhost",        # Local do servidor PostgreSQL
    "port": "5432"              # Porta padrão do PostgreSQL
}

try:
    # Criando a conexão
    conn = psycopg2.connect(**DB_CONFIG)

    # Criando um cursor para interagir com o banco
    cursor = conn.cursor()

    # Executando uma consulta simples
    cursor.execute("SELECT version();")
    versao = cursor.fetchone()

    print(f"Conectado com sucesso! 🚀")
    print(f"Versão do PostgreSQL: {versao[0]}")

    # Fechar a conexão
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Erro ao conectar ao PostgreSQL: {e}")
