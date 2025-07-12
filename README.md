# Crypto Data Collector

Aplicação Python para **coleta e armazenamento de dados de criptomoedas** via [CoinCap API](https://docs.coincap.io/).

Armazena os dados em um banco **PostgreSQL hospedado no GCP (Cloud SQL)**.

Desenvolvido como parte de um desafio técnico, seguindo boas práticas de clean code, modularização e configuração externa.

---

## Funcionalidades

- Conexão com API pública de criptomoedas
- Coleta de dados como:
  - nome
  - símbolo
  - rank
  - preço
  - market cap
  - volume 24h
  - variação 24h
- Armazenamento em banco relacional (PostgreSQL)
- Criação automática de tabelas
- Configuração via variáveis de ambiente
- Código modular e organizado

---

## Estrutura do Projeto

crypto_data_collector/
│
├── api/
│ └── coincap_client.py
│
├── db/
│ ├── connection.py
│ ├── models.py
│ └── repository.py
│
├── config/
│ └── settings.py
│
├── main.py
├── requirements.txt
├── .env
├── README.md


---

## Pré-requisitos

* Python 3.10 ou superior  
* PostgreSQL (Cloud SQL no GCP ou local)

---

## Instalação

* Clone o repositório:

```bash
git clone https://github.com/josecmachado/crypto_data_collector.git
cd crypto_data_collector

    Crie o ambiente virtual:

python -m venv venv

    Ative o ambiente virtual:

    Windows (PowerShell):

.\venv\Scripts\Activate


pip install -r requirements.txt

---

## Configuração

    Copie o arquivo .env.example:

cp .env.example .env

    Edite o .env com suas credenciais do banco e da API:

DB_HOST=<IP_da_sua_instância_Cloud_SQL>
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASS=SuaSenhaSegura

API_BASE_URL=https://api.coincap.io/v2

## Como Executar

Rode o script principal:

python main.py

## O script irá:

    Criar as tabelas no banco, se não existirem

    Coletar dados da CoinCap API

    Armazenar as informações no PostgreSQL

## Estrutura do Banco de Dados

O projeto cria duas tabelas:

* cryptocurrency

Coluna	Tipo
id	VARCHAR(50) PK
name	VARCHAR(255)
symbol	VARCHAR(50)
rank	INTEGER

* crypto_market_data

Coluna	Tipo
id	SERIAL PK
crypto_id	FK para cryptocurrency(id)
timestamp	TIMESTAMP
price_usd	NUMERIC
market_cap_usd	NUMERIC
volume_usd_24h	NUMERIC
change_pct_24h	NUMERIC

## Exemplo de Saída

DB SETTINGS LIDOS DO .env: {'host': '34.44.118.166', 'port': 5432, ...}
Dados inseridos com sucesso!

* Observações

    Caso veja o erro:

O arquivo .\venv\Scripts\Activate.ps1 não pode ser carregado porque a execução de scripts foi desabilitada neste sistema.

* Rode no PowerShell (administrador):

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force