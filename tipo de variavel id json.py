import json

# Abrir o arquivo JSON
json_path = "Ano-2022.json"  # Verifique o nome correto do arquivo
with open(json_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Pegar o primeiro ID encontrado no JSON
exemplo_id = data["dados"][0]["numeroDeputadoID"]
print(f"🔍 Exemplo de ID do JSON: {exemplo_id} ({type(exemplo_id)})")
