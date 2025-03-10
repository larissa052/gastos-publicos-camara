import requests
import psycopg2

# Configuração do banco de dados
# Configuração da conexão
DB_CONFIG = {
    "dbname": "GASTOS_CAMARA",  # Nome do banco de dados
    "user": "postgres",         # Usuário
    "password": "larissa5",    # Senha do usuário
    "host": "localhost",        # Local do servidor PostgreSQL
    "port": "5432"              # Porta padrão do PostgreSQL
}

# Conectar ao PostgreSQL
conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

# Obter lista de deputados
url_deputados = "https://dadosabertos.camara.leg.br/api/v2/deputados"
response = requests.get(url_deputados)
deputados = response.json()["dados"]

# Inserir deputados no banco
for dep in deputados:
    cursor.execute("""
        INSERT INTO tb_deputados (id, nome, partido, estado) 
        VALUES (%s, %s, %s, %s) 
        ON CONFLICT (id) DO NOTHING;
    """, (dep["id"], dep["nome"], dep["siglaPartido"], dep["siglaUf"]))

conn.commit()

# Buscar e armazenar gastos
for dep in deputados:
    id_deputado = dep["id"]
    url_gastos = f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}/despesas?ano=2022"
    response_gastos = requests.get(url_gastos)
    despesas = response_gastos.json()["dados"]

    for despesa in despesas:
        cursor.execute("""
            INSERT INTO tb_gastos (co_deputado, data, tp_despesa, valor) 
            VALUES (%s, %s, %s, %s);
        """, (id_deputado, despesa["dataDocumento"], despesa["tipoDespesa"], despesa["valorDocumento"]))

conn.commit()

print("Dados da API carregados com sucesso!")

cursor.close()
conn.close()
