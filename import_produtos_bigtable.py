"""Importa produtos de um CSV para uma tabela do Google Bigtable.

O CSV deve ter as colunas: nome, preco, categoria, estoque, avaliacoes.
Cada produto vira uma linha na tabela usando `nome` como row key.
"""

from google.cloud import bigtable
import csv

# Configuração do Bigtable e do CSV
project_id = "project-540309eb-bfe6-43d5-ab8"
instance_id = "columndb"
table_id = "produto"
csv_path = "produtos.csv"

# Conecta ao cliente Bigtable e seleciona instância/tabela
client = bigtable.Client(project=project_id, admin=True)
instance = client.instance(instance_id)
table = instance.table(table_id)

# Se a tabela não existir, cria a tabela e a família de colunas cf1
if not table.exists():
    print(f"Tabela '{table_id}' não encontrada. Criando tabela e família de colunas 'cf1'...")
    table.create(column_families={"cf1": None})
else:
    # Se a tabela existir, garante a família de colunas cf1
    if "cf1" not in table.list_column_families():
        print("Criando família de colunas 'cf1' na tabela existente...")
        table.column_family("cf1").create()

# Lê o CSV e prepara as linhas para inserir no Bigtable
with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = []

    for item in reader:
        # Usa o nome como chave da linha; troque para outra coluna se precisar de unicidade maior
        row_key = item["nome"].encode("utf-8")
        row = table.direct_row(row_key)

        # Define as células na família cf1
        row.set_cell("cf1", "nome", item["nome"].encode("utf-8"))
        row.set_cell("cf1", "preco", item["preco"].encode("utf-8"))
        row.set_cell("cf1", "categoria", item["categoria"].encode("utf-8"))
        row.set_cell("cf1", "estoque", item["estoque"].encode("utf-8"))
        row.set_cell("cf1", "avaliacoes", item["avaliacoes"].encode("utf-8"))
        rows.append(row)

    # Envia todas as linhas para o Bigtable de uma vez
    statuses = table.mutate_rows(rows)
    
    success_count = 0
    for i, status in enumerate(statuses):
        if status.code == 0:
            success_count += 1
        else:
            row_id = rows[i].row_key.decode("utf-8")
            print(f"Erro ao inserir linha {i} (chave: {row_id}): {status.message}")

    print(f"Importação concluída: {success_count} de {len(rows)} linhas inseridas com sucesso.")
