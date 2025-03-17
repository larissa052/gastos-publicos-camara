import json

json_path = "Ano-2022.json"

with open(json_path, "r", encoding="utf-8") as file:
    dados_json = json.load(file)

sem_data = [gasto for gasto in dados_json.get("dados", []) if gasto["dataEmissao"].strip() == ""]
print(f"🔍 Total de registros sem data: {len(sem_data)}")
