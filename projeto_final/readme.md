# 🎮 Projeto Steam Games NoSQL

Este projeto foi desenvolvido para a disciplina de Banco de Dados NoSQL e implementa uma aplicação completa para trabalhar com dados de jogos da plataforma Steam utilizando dois bancos NoSQL: MongoDB e Redis.

A proposta é coletar informações públicas por meio de uma API externa, armazenar os dados de forma documental no MongoDB e usar o Redis para criar rankings e consultas rápidas baseadas em métricas de jogos.

---

# Tecnologias utilizadas

- Python 3
- MongoDB
- Redis
- PyMongo
- Redis-py
- Requests
- urllib3
- Visual Studio Code

---

# Estrutura do projeto

```text
projeto_final/
├── aplicacao_menu_games.py     # Menu interativo no terminal para CRUD e rankings
├── etl_jogos.py                # Script de extração, transformação e carga dos dados
├── mongo.py                    # Conexão com o MongoDB
├── mongo_crud.py               # Operações CRUD no MongoDB
├── redis_db.py                 # Conexão com o Redis
├── redis_service.py            # Geração de rankings e consultas no Redis
├── start_redis.bat             # Script para iniciar o servidor Redis no Windows
├── tests/
│   ├── test_api.py
│   ├── test_python_mongodb.py
│   ├── test_python_redis.py
│   └── teste_redis_ranking.py
└── readme.md                   # Documentação do projeto
```

---

# Fonte dos dados

Os dados são obtidos da API pública do SteamSpy:

https://steamspy.com/api.php

O script de ETL acessa a API, recupera os jogos disponíveis e transforma os campos em um formato adequado para armazenamento.

---

# Banco de dados e modelagem

## MongoDB

O MongoDB é utilizado como banco principal de persistência dos dados dos jogos.

### Coleção
- jogos

### Modelo de documento
Cada documento representa um jogo com campos como:

- appid
- name
- developer
- publisher
- positive
- negative
- price
- owners
- average_forever
- average_2weeks
- median_forever
- median_2weeks
- ccu
- score_rank

Essa modelagem é adequada para um banco NoSQL documental, pois cada jogo é armazenado como um único documento, sem necessidade de joins complexos.

## Redis

O Redis é utilizado para acelerar consultas e gerar rankings em tempo de execução.

### Estruturas usadas
- Sorted sets (conjuntos ordenados)

### Rankings armazenados
- jogos mais positivos
- jogos mais negativos
- jogos mais caros
- jogos mais baratos
- jogos com mais jogadores online

Cada ranking é armazenado com o nome do jogo e uma pontuação numérica associada.

---

# Funcionalidades

- Extrair dados da API SteamSpy
- Transformar e carregar os dados no MongoDB
- Listar jogos cadastrados
- Buscar jogos por AppID
- Buscar jogos por nome
- Inserir novos jogos manualmente
- Atualizar informações de jogos existentes
- Excluir jogos do banco
- Gerar rankings no Redis
- Consultar rankings por diferentes critérios

---

# Como executar

## 1. Pré-requisitos

- Ter o MongoDB instalado e em execução
- Ter o Redis instalado e em execução
- Python 3 instalado

## 2. Instalar dependências

```bash
pip install requests pymongo redis urllib3
```

## 3. Iniciar os bancos

### MongoDB

O MongoDB pode ser iniciado localmente no servidor padrão:

```bash
mongodb
```

Ou via serviço já configurado no ambiente.

### Redis

No Windows, pode-se usar o script disponibilizado:

```bash
start_redis.bat
```

Ou executar diretamente:

```bash
redis-server
```

## 4. Carregar os dados no MongoDB

```bash
python etl_jogos.py
```

## 5. Executar a aplicação

```bash
python aplicacao_menu_games.py
```

---

# Como o código funciona

## Fluxo de ETL

O script etl_jogos.py realiza três etapas:

1. Extração
   - Faz uma requisição à API do SteamSpy.

2. Transformação
   - Converte os valores recebidos em tipos adequados, como inteiros e strings.

3. Carga
   - Limpa a coleção jogos e insere os novos documentos no MongoDB.

## Fluxo da aplicação

O arquivo aplicacao_menu_games.py cria um menu interativo no terminal.

A partir dele, o usuário pode:
- listar jogos
- buscar por AppID
- buscar por nome
- inserir novos jogos
- atualizar dados
- excluir jogos
- gerar rankings no Redis
- visualizar rankings diversos

## Arquitetura dos módulos

- mongo.py: define a conexão com o MongoDB e a coleção jogos
- mongo_crud.py: centraliza as operações de CRUD
- redis_db.py: define a conexão com o Redis
- redis_service.py: gera e consulta os rankings salvos no Redis

---

# O que cada banco de dados faz

## MongoDB

O MongoDB é responsável por armazenar os dados principais de forma permanente e estruturada como documentos. Ele serve como fonte de verdade para consulta, cadastro e atualização dos jogos.

## Redis

O Redis é usado para armazenar rankings e dados que precisam de acesso rápido. Ele funciona como camada de desempenho e consulta ágil para listas ordenadas, como os jogos mais avaliados ou mais caros.

---

# Objetivo

O objetivo principal deste projeto é demonstrar a utilização conjunta de dois bancos de dados NoSQL em uma aplicação prática.

- O MongoDB é usado para armazenamento documental e manipulação de dados completos dos jogos.
- O Redis é usado para otimizar consultas e disponibilizar rankings de forma rápida.

Com isso, o projeto mostra como integrar diferentes modelos de banco NoSQL em uma solução realista, com extração de dados externos, persistência, consultas e análise.

