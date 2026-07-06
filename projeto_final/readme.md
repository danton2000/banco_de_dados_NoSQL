# 🎮 Steam Games API

Projeto desenvolvido para a disciplina de Banco de Dados NoSQL.

A aplicação realiza a importação de informações de jogos da plataforma Steam utilizando a API pública SteamSpy. Os dados são armazenados no MongoDB e o Redis é utilizado para cache e rankings, sendo disponibilizados através de uma API REST desenvolvida com Flask.

---

# Tecnologias

* Python
* Flask
* MongoDB
* Redis
* Requests

---

# Estrutura do Projeto

```text
projeto/

├── app.py
├── importar_jogos.py
├── requirements.txt
└── README.md
```

---

# Fonte dos Dados

Os dados utilizados são obtidos através da API pública SteamSpy.

https://steamspy.com/api.php

---

# Banco de Dados

## MongoDB

Responsável pelo armazenamento permanente das informações dos jogos.

Coleção utilizada:

* jogos

Cada documento poderá conter informações como:

* AppID
* Nome
* Desenvolvedora
* Publicadora
* Gêneros
* Preço
* Quantidade estimada de proprietários
* Avaliações positivas
* Avaliações negativas
* Tempo médio de jogo

## Redis

Utilizado para armazenamento de dados de acesso rápido.

Estruturas previstas:

* Ranking dos jogos mais populares.
* Ranking dos jogos mais bem avaliados.
* Cache de consultas.

---

# Funcionalidades

* Importar jogos da SteamSpy.
* Listar todos os jogos.
* Buscar jogo por nome.
* Buscar jogos por gênero.
* Buscar jogos por desenvolvedora.
* Atualizar informações de um jogo.
* Remover jogos.
* Consultar rankings armazenados no Redis.

---

# Como executar

## Instalar as dependências

```bash
pip install -r requirements.txt
```

## Executar o MongoDB

Inicie o servidor MongoDB localmente.

## Executar o Redis

Inicie o servidor Redis localmente.

## Importar os dados

```bash
python importar_jogos.py
```

## Executar a API

```bash
python app.py
```

---

# Objetivo

Demonstrar a utilização conjunta de dois bancos de dados NoSQL em uma aplicação prática.

O MongoDB será responsável pelo armazenamento documental das informações dos jogos, enquanto o Redis será utilizado para armazenamento temporário, cache de consultas e rankings, explorando as características e vantagens de cada tecnologia.

## Levantar os bancos de dados(localmente)

### Redis

Executar os scripts local
"C:\Users\danto\Downloads\Redis-8.8.0-Windows-x64-cygwin-with-Service\start.bat"

"C:\Users\danto\Downloads\Redis-8.8.0-Windows-x64-cygwin-with-Service\redis-cli.exe"

### MongoDB
Ja esta levantando automaticamente