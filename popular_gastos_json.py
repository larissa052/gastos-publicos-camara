import json
import psycopg2

# Configuração do Banco de Dados PostgreSQL
DB_CONFIG = {
    "dbname": "GASTOS_CAMARA",
    "user": "postgres",
    "password": "larissa5",
    "host": "localhost",
    "port": "5432"
}
# Caminho do arquivo JSON
json_path = "Ano-2022.json"

# Conectar ao PostgreSQL
try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    print("✅ Conexão com PostgreSQL bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco: {e}")
    exit()

# Carregar os IDs dos deputados já cadastrados no banco
cursor.execute("SELECT id FROM tb_deputados;")
deputados_banco = {row[0] for row in cursor.fetchall()}
print(f"🔍 Total de deputados no banco: {len(deputados_banco)}")

# Carregar os dados do JSON
try:
    with open(json_path, "r", encoding="utf-8") as file:
        dados_json = json.load(file)
    print("✅ JSON carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar JSON: {e}")
    exit()

# Criar uma lista para armazenar os dados que serão inseridos no banco
gastos_para_inserir = []

# Percorrer os dados do JSON e filtrar os gastos dos deputados que já estão no banco
for gasto in dados_json.get("dados", []):
    try:
        deputado_id = int(gasto["idDeputado"])  # Convertendo ID corretamente

        # Verifica se o deputado está no banco
        if deputado_id in deputados_banco:
            data_emissao = gasto["dataEmissao"].strip()  # Removendo espaços extras

            # Verifica se a data está vazia e substitui por NULL
            data_emissao = data_emissao if data_emissao else None

            gastos_para_inserir.append((
                deputado_id,
                data_emissao,
                gasto["descricao"],  # Tipo de despesa
                float(gasto["valorLiquido"])  # Valor da despesa
            ))
    except (ValueError, KeyError) as e:
        continue  # Ignora erros de formatação

print(f"🔍 Total de gastos filtrados para inserção: {len(gastos_para_inserir)}")

# Inserir os dados filtrados na tabela `tb_gastos`
if gastos_para_inserir:
    try:
        insert_query = """
        INSERT INTO tb_gastos (co_deputado, data, tp_despesa, valor)
        VALUES (%s, %s, %s, %s);
        """
        # Aqui garantimos que None será tratado corretamente como NULL
        cursor.executemany(
            insert_query,
            [(co_deputado, data if data is not None else None, tp_despesa, valor) for co_deputado, data, tp_despesa, valor in gastos_para_inserir]
        )
        
        conn.commit()
        print("Dados de gastos inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir dados no banco: {e}")
        conn.rollback()

# Fechar conexão
cursor.close()
conn.close()
print("Conexão com PostgreSQL encerrada.")