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
    # Conectar ao PostgreSQL
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Inserindo um deputado de teste
    cursor.execute("""
        INSERT INTO tb_deputados (nome, partido, estado) 
        VALUES (%s, %s, %s) RETURNING id;
    """, ("Vicentinho Junior", "XYZ", "TO"))

    deputado_id = cursor.fetchone()[0]  # Pegando o ID gerado automaticamente

    # Inserindo um gasto para esse deputado
    cursor.execute("""
        INSERT INTO tb_gastos (co_deputado, data, tp_despesa, valor) 
        VALUES (%s, %s, %s, %s);
    """, (deputado_id, "2022-01-15", "Hospedagem", 500.00))

    # Confirmar transações
    conn.commit()
    print("Dados inseridos com sucesso!")

except Exception as e:
    print(f"Erro ao inserir dados: {e}")

finally:
    cursor.close()
    conn.close()
