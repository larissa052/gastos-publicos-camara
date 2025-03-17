import requests
import json

# Definir o ano de análise (2022)
ANO_ANALISE = 2022

# URL da API da Câmara dos Deputados para listar deputados ativos
URL_API = "https://dadosabertos.camara.leg.br/api/v2/deputados"

# Parâmetros para buscar deputados da legislatura correta
PARAMS = {"idLegislatura": 56, "itens": 600}  # Legislatura 56 (2019-2022)

print("🔍 Buscando deputados ativos na API da Câmara...")

try:
    response = requests.get(URL_API, params=PARAMS)
    response.raise_for_status()
    data = response.json()
    print("✅ Dados carregados com sucesso!")
except requests.exceptions.RequestException as e:
    print(f"❌ Erro ao acessar a API: {e}")
    exit()

# Criar um conjunto com os IDs dos deputados ativos
deputados_ativos = {int(dep["id"]) for dep in data["dados"]}

print(f"🔍 Total de deputados ativos encontrados na API: {len(deputados_ativos)}")

# Carregar o arquivo JSON com gastos parlamentares
json_path = "Ano-2022.json"

try:
    with open(json_path, "r", encoding="utf-8") as file:
        gastos_json = json.load(file)
    print("✅ JSON de gastos carregado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao carregar JSON: {e}")
    exit()

# Criar um conjunto com os IDs dos deputados do JSON
deputados_json = {int(gasto["numeroDeputadoID"]) for gasto in gastos_json.get("dados", []) if "numeroDeputadoID" in gasto}

print(f"🔍 Total de deputados encontrados no JSON: {len(deputados_json)}")

# Encontrar deputados no JSON que NÃO estão na lista de ativos da API
deputados_extras = deputados_json - deputados_ativos

# Exibir deputados que aparecem no JSON, mas não estão na lista de ativos
if deputados_extras:
    print(f"⚠️ Deputados que aparecem no JSON, mas não estavam ativos na API ({len(deputados_extras)}):")
    for dep_id in sorted(deputados_extras):
        print(dep_id)
else:
    print("✅ Todos os deputados do JSON estavam ativos na API da Câmara!")

