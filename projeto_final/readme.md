# 🏆 CopaDB - Sistema da Copa do Mundo 2026

Projeto desenvolvido para a disciplina de Banco de Dados NoSQL.

A aplicação realiza a importação dos dados da Copa do Mundo de 2026 a partir de um arquivo JSON do projeto OpenFootball, armazenando as informações no MongoDB e utilizando o Redis para consultas rápidas e rankings.

## Tecnologias

* Python
* Flask
* MongoDB
* Redis
* Requests

## Estrutura do Projeto

```text
projeto/

├── app.py
├── importar_dados.py
├── requirements.txt
└── README.md
```

## Fonte dos Dados

Os dados utilizados são obtidos do projeto OpenFootball.

https://github.com/openfootball/worldcup.json

## Banco de Dados

### MongoDB

Responsável pelo armazenamento das partidas da Copa do Mundo.

Coleção utilizada:

* partidas

### Redis

Utilizado para:

* Ranking das seleções
* Ranking de artilheiros
* Cache de consultas

## Funcionalidades

* Importar dados da Copa do Mundo
* Listar partidas
* Buscar partidas por seleção
* Buscar partidas por grupo
* Atualizar partidas
* Remover partidas
* Consultar ranking das seleções

## Como executar

### Instalar as dependências

```bash
pip install -r requirements.txt
```

### Executar o MongoDB

Inicie o servidor MongoDB localmente.

### Executar o Redis

Inicie o servidor Redis localmente.

### Importar os dados

```bash
python importar_dados.py
```

### Executar a API

```bash
python app.py
```

## Objetivo

Demonstrar a utilização de dois bancos de dados NoSQL em uma mesma aplicação, utilizando o MongoDB para armazenamento documental e o Redis para consultas rápidas e armazenamento temporário.
