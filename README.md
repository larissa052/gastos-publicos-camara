# 🏛️ Gastos Públicos da Câmara dos Deputados

Este projeto coleta, armazena e analisa os **gastos parlamentares** dos deputados federais do Brasil usando a **API da Câmara dos Deputados** e um banco de dados **PostgreSQL**. Além disso, o projeto identifica que **a API não fornece gastos anteriores a 2023**, sendo necessário buscar esses dados no **Portal da Transparência**.

---

## 📌 **Objetivo do Projeto**
O objetivo deste projeto é garantir **transparência pública**, permitindo que qualquer pessoa possa acessar e analisar os gastos dos parlamentares de forma clara e acessível.  

✅ Consultar os deputados e seus gastos diretamente da API da Câmara.  
✅ Armazenar os dados em um banco de dados relacional (PostgreSQL).  
✅ Identificar padrões nos gastos e gerar insights.  
✅ Destacar a ausência de dados históricos antes de 2023 na API.

---

## 🛠 **Tecnologias Utilizadas**
- **Python** → Para buscar e processar os dados.  
- **PostgreSQL** → Para armazenar os dados.  
- **Requests** → Para consumir a API da Câmara dos Deputados.  
- **Psycopg2** → Para conectar Python ao banco de dados PostgreSQL.  
- **Git e GitHub** → Para controle de versão e colaboração.  

---

## 🚀 **Como Configurar o Projeto**

### 1️⃣ **Instale as dependências**
```bash
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
3️⃣ Execute o script para buscar os dados da API
bash
Copy
Edit
python buscar_dados_api.py
Isso vai:

Baixar todos os deputados ativos e armazená-los na tb_deputados.
Baixar os gastos parlamentares e armazená-los na tb_gastos.
4️⃣ Verifique os dados no banco
No pgAdmin ou no terminal SQL do PostgreSQL, execute:

sql
Copy
Edit
SELECT * FROM tb_deputados;
SELECT * FROM tb_gastos;
