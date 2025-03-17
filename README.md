🏛️ Gastos Públicos da Câmara dos Deputados
Este projeto coleta, armazena e analisa os gastos parlamentares dos deputados federais do Brasil usando a API da Câmara dos Deputados e um banco de dados PostgreSQL. Além disso, buscamos dados adicionais do Portal da Transparência e do JSON de 2022 para complementar as informações da API.

📌 Objetivo do Projeto
O objetivo deste projeto é garantir transparência pública, permitindo que qualquer pessoa possa acessar e analisar os gastos dos parlamentares de forma clara e acessível.

✅ Consultar os deputados e seus gastos diretamente da API da Câmara.
✅ Armazenar os dados em um banco de dados relacional (PostgreSQL).
✅ Enriquecer os dados com informações do JSON de 2022.
✅ Identificar padrões nos gastos e gerar insights.
✅ Destacar a ausência de dados completos para 2022 na API.

📊 Principais Descobertas
Após análise detalhada dos dados, descobrimos que:

🔹 A API da Câmara disponibiliza gastos de apenas 32 deputados em 2022.
🔹 O JSON de 2022 contém gastos de 232 deputados, um número significativamente maior.
🔹 Após inserir os dados do JSON no banco, passamos de 32 para 281 deputados com gastos registrados.
🔹 No entanto, 3265 registros de gastos possuem data NULL, o que pode impactar algumas análises.

Essa diferença mostra que a API não fornece todos os dados históricos, tornando essencial o uso do JSON para garantir um banco de dados mais completo.

🛠 Tecnologias Utilizadas
Python → Para buscar e processar os dados.
PostgreSQL → Para armazenar os dados.
Requests → Para consumir a API da Câmara dos Deputados.
Psycopg2 → Para conectar Python ao banco de dados PostgreSQL.
Git e GitHub → Para controle de versão e colaboração.
🚀 Como Configurar o Projeto
1️⃣ Instale as dependências
bash
Copy
Edit
pip install requests psycopg2-binary
2️⃣ Configure o Banco de Dados PostgreSQL
Crie um banco chamado gastos_camara no PostgreSQL.
Execute os scripts SQL para criar as tabelas:
sql
Copy
Edit
CREATE TABLE tb_deputados (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    partido VARCHAR(50),
    estado VARCHAR(50)
);

CREATE TABLE tb_gastos (
    id SERIAL PRIMARY KEY,
    co_deputado INT REFERENCES tb_deputados(id),
    data DATE,
    tp_despesa VARCHAR(255),
    valor NUMERIC(10,2)
);
3️⃣ Execute os scripts para coletar e inserir os dados
🔹 Buscar dados da API
bash
Copy
Edit
python buscar_dados_api.py
✔️ Isso baixa todos os deputados ativos e seus gastos diretamente da API e insere no banco.

🔹 Inserir dados do JSON de 2022 no banco
bash
Copy
Edit
python popular_gastos_json.py
✔️ Esse script complementa os dados do banco com informações mais completas do JSON de 2022.

4️⃣ Verifique os dados no banco
No pgAdmin ou no terminal SQL do PostgreSQL, execute:

sql
Copy
Edit
SELECT COUNT(*) FROM tb_deputados;
SELECT COUNT(*) FROM tb_gastos WHERE data IS NULL;
Essas consultas ajudam a conferir a quantidade de registros e verificar quantos gastos ficaram com data NULL.

📜 Licença
Este projeto é de código aberto e pode ser usado para fins acadêmicos ou estudos.

📩 Dúvidas?
Se precisar de ajuda ou sugestões, sinta-se à vontade para abrir uma issue ou contribuir! 🚀

