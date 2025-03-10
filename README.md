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
