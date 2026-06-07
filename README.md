# API Data Ingestion Pipeline

Pipeline de Engenharia de Dados desenvolvido em Python para ingestão, transformação e análise de dados provenientes de uma API REST pública.

O projeto implementa uma arquitetura em camadas (Raw → Bronze → Silver → Gold), simulando um fluxo moderno de processamento de dados utilizado em ambientes corporativos.

![alt text](<api-data-ingestion-pipeline - architecture.png>)

---

## Objetivo

Demonstrar na prática conceitos fundamentais de Engenharia de Dados:

- Consumo de APIs REST
- Extração de dados em JSON
- Conversão para Parquet
- Normalização de dados semi-estruturados
- Modelagem em camadas (Medallion Architecture)
- Criação de datasets analíticos
- Geração de KPIs para análise de negócio

---

## Tecnologias Utilizadas

- Python
- Pandas
- Requests
- PyArrow
- Jupyter Notebook

---

## Arquitetura
```
Fake Store API
↓
Extract
↓
Raw (JSON)
↓
Bronze (Parquet)
↓
Silver (Dados Normalizados)
↓
Gold (KPIs)
```
---

## Estrutura do Projeto

```
api-data-ingestion-pipeline/

├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── notebooks/
│   ├── exploration.ipynb
│   ├── exploration_silver.ipynb
│   ├── exploration_gold.ipynb
│   └── validate_gold.ipynb
│
├── src/
│   ├── extract.py
│   ├── bronze.py
│   ├── silver.py
│   └── gold.py
│
├── requirements.txt
├── .gitignore
└── README.md
```
---

## Camadas do Pipeline

### Raw Layer

Responsável pela extração dos dados da API Fake Store.

Arquivos gerados:

- products.json
- users.json
- carts.json

---

### Bronze Layer

Conversão dos arquivos JSON para formato Parquet.

Arquivos gerados:

- products.parquet
- users.parquet
- carts.parquet

Benefícios:

- Melhor compressão
- Melhor performance de leitura
- Formato amplamente utilizado em Data Lakes

---

### Silver Layer

Normalização dos dados semi-estruturados.

Transformações realizadas:

#### Products

Expansão da estrutura:

rating

em:

- rating_rate
- rating_count

#### Users

Expansão de:

- name
- address
- geolocation

Remoção de campos sensíveis:

- password

#### Carts

Explosão da lista de produtos para geração da tabela:

cart_items

---

### Gold Layer

Criação de datasets analíticos para consumo por dashboards e análises.

KPIs gerados:

- Produtos por categoria
- Preço médio por categoria
- Quantidade vendida por produto
- Top produtos
- Top usuários

Arquivos gerados:

- products_by_category.parquet
- avg_price_by_category.parquet
- product_sales.parquet
- top_products.parquet
- top_users.parquet

---

## Exemplos de KPIs

### Produtos por Categoria

| Categoria | Total |
|------------|--------|
| Electronics | 6 |
| Jewelery | 4 |
| Men's Clothing | 4 |
| Women's Clothing | 6 |

---

## Como Executar

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Executar extração
```bash
python src/extract.py
```

### Executar bronze
```bash
python src/bronze.py
```

### Executar Silver
```bash
python src/silver.py
```

### Gold
```bash
python src/gold.py
```

## Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos de:

* Engenharia de Dados
* ETL
* APIs REST
* JSON
* Parquet
* Data Lake
* Medallion Architecture
* Normalização de dados
* Agregações analíticas
* Joins
* KPIs de negócio

## Próximas Evoluções

Possíveis melhorias futuras:

* Orquestração com Apache Airflow
* Containerização com Docker
* Processamento distribuído com PySpark
* Testes automatizados
* Deploy em ambiente cloud