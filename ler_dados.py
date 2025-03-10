import psycopg2

# Conectar ao PostgreSQL
conn = psycopg2.connect(
    dbname="GASTOS_CAMARA",
    user="postgres",
    password="senha",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Buscar todos os deputados
cursor.execute("SELECT * FROM tb_deputados;")
deputados = cursor.fetchall()

print("Lista de Deputados:")
for dep in deputados:
    print(dep)

# Buscar todos os gastos
cursor.execute("""
    SELECT g.id, d.nome, g.data, g.tp_despesa, g.valor 
    FROM tb_gastos g
    JOIN tb_deputados d ON g.co_deputado = d.id;
""")
gastos = cursor.fetchall()

print("\nLista de Gastos:")
for gasto in gastos:
    print(gasto)

cursor.close()
conn.close()
