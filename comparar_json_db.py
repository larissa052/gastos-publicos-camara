import json
import psycopg2

# Caminho do arquivo JSON
json_path = "Ano-2022.json"

# Tentar carregar o JSON
try:
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    print("JSON carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar JSON: {e}")
    exit()

# Definir a legislatura correta para 2022
LEGISLATURA_ATUAL = 56  

# Criar um conjunto (set) para armazenar IDs dos deputados do JSON (evita duplicatas)
deputados_json = set()

for gasto in data.get("dados", []):  
    try:
        deputado_id = int(gasto["idDeputado"])  # ALTERADO: Usando "idDeputado" agora
        legislatura = int(gasto["codigoLegislatura"])  
        
        # Filtrar apenas os deputados da legislatura correta
        if legislatura == LEGISLATURA_ATUAL:
            deputados_json.add(deputado_id)
    except (ValueError, KeyError):
        continue  

# Total de deputados no JSON
total_deputados_json = len(deputados_json)
print(f"Total de IDs únicos no JSON (Legislatura {LEGISLATURA_ATUAL}): {total_deputados_json}")

# Conectar ao PostgreSQL
DB_CONFIG = {
    "dbname": "GASTOS_CAMARA",
    "user": "postgres",
    "password": "larissa5",
    "host": "localhost",
    "port": "5432"
}

try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    print("Conexão com PostgreSQL bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco: {e}")
    exit()

# Buscar IDs dos deputados no banco
try:
    cursor.execute("SELECT id FROM tb_deputados;")
    deputados_db = {row[0] for row in cursor.fetchall()}  # Criar conjunto (set) com IDs
    total_deputados_db = len(deputados_db)
    print(f"🔍 Total de IDs únicos no Banco de Dados: {total_deputados_db}")
except Exception as e:
    print(f"Erro ao buscar deputados no banco: {e}")
    exit()

# Encontrar IDs que estão no banco, mas não no JSON
faltantes = deputados_db - deputados_json  # ALTERADO: Agora compara os IDs do banco que NÃO estão no JSON

# Quantidade correta de deputados no banco, mas não no JSON
total_faltantes = len(faltantes)

print(f"Deputados que estão no banco, mas não no JSON: {total_faltantes}")

# Exibir apenas a lista de IDs dos deputados que estão no banco, mas não no JSON
if faltantes:
    print("Lista de IDs de deputados que estão no banco, mas não no JSON:")
    for deputado_id in faltantes:
        print(f"ID: {deputado_id}")

# Fechar conexão
cursor.close()
conn.close()
